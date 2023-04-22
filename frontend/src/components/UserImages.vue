<template>
    <div class="user-images container">
        <h2 class="my-4">User Images</h2>
        <div v-if="isLoading" class="text-center">
            <div class="spinner-border" role="status">
                <span class="sr-only"></span>
            </div>
        </div>
        <div v-else class="row">
            <div class="col-md-4 col-sm-6 mb-4" v-for="image in images" :key="image.id">
                <div class="card bg-dark">
                    <img :src="image.url" :alt="image.id" class="image-container card-img"/>
                    <h3 class="text-white">Test Test</h3>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import axios from "axios";

export default {
    name: "UserImages",
    compatConfig: {
        MODE: 3
    },
    data() {
        return {
            images: [],
            isLoading: true,
        };
    },
    async created() {
        try {
            const token = localStorage.getItem("access_token");
            const response = await axios.get("http://localhost:5000/api/images", {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });
            const imageData = response.data;
            for (const image of imageData) {
                const response = await axios.get(`http://localhost:5000/api/images/${image.id}`, {
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                    responseType: 'blob'
                });
                const imageURL = URL.createObjectURL(response.data);
                console.log(imageURL);
                this.images.push(
                    {
                        id: image.id,
                        url: imageURL,
                    }
                );
            }
        } catch (error) {
            console.error("Error fetching images:", error);
        } finally {
            this.isLoading = false;
        }
    },
};
</script>
<style scoped>
</style>