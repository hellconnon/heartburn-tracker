<template>
  <div>
    <Sidebar />
    <div class="content">
      <router-view />
    </div>
  </div>
</template>

<script>
import Sidebar from "./components/Sidebar.vue";

export default {
  components: {
    Sidebar,
  },
};
</script>

<style scoped>
.content {
  margin-left: 240px; /* Adjust this value according to the width of your sidebar */
}
</style>
