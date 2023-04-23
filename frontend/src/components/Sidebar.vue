<template>
  <div
    class="flex flex-col pt-1 w-16 bg-gray-900 text-white shadow-sm top-0 left-0 h-screen m-0"
  >
      <NavLink
        :is-open="isOpen"
        text="Home"
        icon="fas fa-home"
        to="/"
      ></NavLink>
      <NavLink
        :is-open="isOpen"
        text="Images"
        icon="fas fa-images"
        to="/user-images"
      ></NavLink>
      <NavLink
        :is-open="isOpen"
        text="Recipes"
        icon="fas fa-utensils"
        to="/recipes"
      ></NavLink>
      <NavLink
        :is-open="isOpen"
        text="Ingredients"
        icon="fas fa-carrot"
        to="/ingredients"
      ></NavLink>
  </div>
</template>

<script>
import NavLink from "@/components/NavLink.vue";

export default {
  name: "Sidebar",
  components: { NavLink },
  data() {
    return {
      isOpen: false,
    };
  },
};
</script>
