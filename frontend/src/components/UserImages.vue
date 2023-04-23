<template>
    <div class="flex">

        <Sidebar/>

        <div class="flex-grow bg-gray-900 min-h-screen text-white">
            <div class="container mx-auto px-4 py-8">
                <h2 class="text-2xl mb-8">User Images</h2>
                <div v-if="isLoading" class="flex justify-center text-white">
                    <div class="spinner-border" role="status">
                        <span class="sr-only"></span>
                    </div>
                </div>
                <div v-else class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                    <div v-for="image in images" :key="image.id">
                        <div class="bg-gray-800 rounded overflow-hidden">
                            <img :src="image.url" :alt="image.id" class="w-full h-auto"/>
                            <h3 class="text-center py-2">Test Test</h3>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import Sidebar from "@/components/Sidebar.vue";

export default {
    name: "UserImages",
    components: {Sidebar},
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
