<template>
    <div class="flex">
        <div class="w-50 h-auto bg-gray-900">
            <nav class="px-4">
                <ul class="flex flex-col space-y-4">
                    <li>
                        <button class="p-5 flex items-center justify-center w-10 h-10 bg-gray-700 text-white rounded-md hover:bg-gray-600 focus:outline-none transition-all duration-200 ease-in-out"
                                @click="isOpen = !isOpen">
                            <i :class="isOpen ? 'fas fa-angle-left' : 'fas fa-angle-right'"></i>
                        </button>
                    </li>
                    <NavLink :is-open="isOpen" text="Home" icon="fas fa-home" to="/"></NavLink>
                    <NavLink :is-open="isOpen" text="Images" icon="fas fa-images" to="/user-images"></NavLink>
                    <NavLink :is-open="isOpen" text="Recipes" icon="fas fa-utensils" to="/recipes"></NavLink>
                    <NavLink :is-open="isOpen" text="Ingredients" icon="fas fa-carrot" to="/ingredients"></NavLink>
                </ul>
            </nav>
        </div>
    </div>

</template>

<script>
import NavLink from "@/components/NavLink.vue";

export default {
    name: "Sidebar",
    components: {NavLink},
    data() {
        return {
            isOpen: false,
        };
    },
};
</script>
