<template>
  <div class="flex pr-4">
    <Sidebar />

    <div class="pl-8 pt-4 grid grid-cols-3 gap-4 h-full w-full">
      <div class="col-span-1">
        <div class="flex items-center justify-between mb-4">
          <h2 class="sticky text-3xl text-white font-bold">Recipes</h2>
          <div class="flex items-center justify-end">
            <button
              class="fas fa-plus text-white border rounded-full w-8 h-8 hover:bg-white hover:text-blue-700 mr-2"
              @click="showAddRecipe = true"
            ></button>
            <button
              class="fas fa-filter text-white border rounded-full w-8 h-8 hover:bg-white hover:text-blue-700 mr-2"
            ></button>
            <button
              class="fas fa-sort text-white border rounded-full w-8 h-8 hover:bg-white hover:text-blue-700"
            ></button>
          </div>
        </div>

        <div class="space-y-2">
          <RecipeListItem
            v-for="(recipe, index) in recipes"
            :key="index"
            :recipe-name="recipe.name"
            :recipe-count="recipe.count"
            :selected="index === selectedIndex"
            @select="selectRecipe(index)"
          />
        </div>
      </div>
      <div
        class="col-span-2 p-4 rounded-3xl text-white"
        :class="{ border: selectedRecipe }"
      >


        <div v-if="showAddRecipe" class="border">
        <AddRecipeDialog @close="showAddRecipe = false"/>
        </div>


        <div v-if="selectedRecipe">
          <h2 class="text-lg font-bold mb-4">{{ selectedRecipe.name }}</h2>
          <p class="text-sm text-gray-600 mb-4">
            {{ selectedRecipe.count }} recipes
          </p>
          <p class="mb-4">{{ selectedRecipe.description }}</p>
          <h3 class="font-bold mb-2">Ingredients</h3>
          <ul class="list-disc pl-4">
            <li
              v-for="ingredient in selectedRecipe.ingredients"
              :key="ingredient"
            >
              {{ ingredient }}
            </li>
          </ul>
          <button
            class="mt-4 text-white bg-red-500 hover:bg-red-600 px-4 py-2 rounded-md focus:outline-none"
            @click="deleteRecipe(selectedIndex)"
          >
            Delete
          </button>
        </div>
        <div v-else class="flex items-center justify-center h-full">
          <p class="text-lg text-white font-bold p-5">
            Select a recipe to view details
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Sidebar from "./Sidebar.vue";
import RecipeListItem from "@/components/RecipeListItem.vue";
import AddRecipeDialog from '@/components/AddRecipeDialog.vue'

export default {
  name: "Recipes",
  components: { RecipeListItem, Sidebar, AddRecipeDialog },
  data() {
    return {
      showAddRecipe: false,
      recipes: [
        {
          name: "Pasta",
          count: 42,
          description: "A delicious Italian dish",
          ingredients: ["pasta", "tomato sauce", "cheese"],
        },
        {
          name: "Pizza",
          count: 8,
          description: "A classic Italian dish",
          ingredients: ["dough", "tomato sauce", "cheese", "toppings"],
        },
        {
          name: "Burger",
          count: 6,
          description: "A classic American dish",
          ingredients: ["buns", "beef patty", "lettuce", "tomato", "cheese"],
        },
      ],
      selectedIndex: -1,
    };
  },
  methods: {
    deleteRecipe(index) {
      this.recipes.splice(index, 1);
      this.selectedIndex = -1;
    },
    selectRecipe(index) {
      this.selectedIndex = index;
    },
  },
  computed: {
    selectedRecipe() {
      return this.selectedIndex !== -1
        ? this.recipes[this.selectedIndex]
        : null;
    },
  },
};
</script>
