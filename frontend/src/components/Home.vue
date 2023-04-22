<template>
  <div class="bg-dark text-white d-flex flex-column vh-100">
      <h1 class="display-4 mb-4">Dashboard</h1>
      <div class="container my-auto">
      <div class="row">
        <div v-for="i in 4" :key="i" class="col-lg-3 col-md-6 mb-4">
          <div class="card p-5 h-auto">
            <h3 class="card-title text-dark">Item {{ i }}</h3>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
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
