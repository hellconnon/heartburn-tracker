<template>

    <div class="flex">

        <Sidebar/>

        <div class="flex-grow min-h-screen bg-gray-100">
            <div class="container mx-auto px-4 py-8">
                <h1 class="text-4xl mb-6">Dashboard</h1>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    <div class="bg-white rounded shadow p-6">
                        <h2 class="text-2xl mb-4">Recipes</h2>
                        <p>Total recipes: 25</p>
                    </div>
                    <div class="bg-white rounded shadow p-6">
                        <h2 class="text-2xl mb-4">Ingredients</h2>
                        <p>Total ingredients: 120</p>
                    </div>
                    <div class="bg-white rounded shadow p-6">
                        <h2 class="text-2xl mb-4">Images</h2>
                        <p>Total images: 35</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Sidebar from "./Sidebar.vue";

export default {
    name: "Home",
    components: {Sidebar},
};
</script>

<style scoped>
.home-dashboard {
    box-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
}

.home-dashboard h1,
.home-dashboard h3 {
    text-shadow: 0 0 5px rgba(0, 255, 255, 0.5);
}

.dashboard-item {
    background-color: rgba(255, 255, 255, 0.1);
    border-radius: 1rem;
    box-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
}
</style>
