<template>
  <div
    class="flex flex-col pt-1 w-16 bg-gray-950 text-white top-0 left-0 h-screen m-0"
  >
    <NavLink text="Home" icon="fas fa-home" to="/"></NavLink>
    <NavLink text="Images" icon="fas fa-images" to="/user-images"></NavLink>
    <NavLink text="Recipes" icon="fas fa-utensils" to="/recipes"></NavLink>
    <NavLink
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
  },
};
</script>
