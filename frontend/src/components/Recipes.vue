<template>
    <div class="row">
      <div class="col-md-6">
        <ul class="list-group">
          <li
            v-for="(recipe, index) in recipes"
            :key="index"
            class="bg-dark text-light list-group-item recipe-item"
          >
            {{ recipe.name }}
          </li>
        </ul>
      </div>
      <div class="col-md-6">
        <div class="content-area bg-dark text-light rounded p-3">
          <h2 class="text-center mb-4">{{ selectedRecipe.title }}</h2>
          <!-- Add more content here -->
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: "Recipes",
  data() {
    return {
      recipes: [
        { name: "Recipe 1" },
        { name: "Recipe 2" },
        { name: "Recipe 3" },
        { name: "Recipe 4" },
      ],
      selectedRecipe: { title: "Selected Recipe" },
    };
  },
};
</script>

<style scoped>
/*.recipe-item:hover {*/
/*  background-color: rgba(255, 255, 255, 0.1);*/
/*  cursor: pointer;*/
/*}*/
</style>
