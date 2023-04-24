<template>
  <div class="fixed z-10 inset-0 overflow-y-auto">
    <div
      class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0"
    >
      <div
        class="fixed inset-0 transition-opacity"
        aria-hidden="true"
        @click.self="$emit('close')"
      >
        <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
      </div>
      <span
        class="hidden sm:inline-block sm:align-middle sm:h-screen"
        aria-hidden="true"
        >&#8203;</span
      >
      <div
        class="inline-block bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all my-8 align-middle max-w-lg w-full"
        role="dialog"
        aria-modal="true"
        aria-labelledby="modal-headline"
      >
        <div class="px-4 pt-5 pb-4 sm:p-6 sm:pb-4 text-gray-700">
          <form class="space-y-6">
            <div>
              <label for="recipe-name" class="block text-sm font-medium"
                >Recipe Name</label
              >
              <input
                type="text"
                id="recipe-name"
                name="recipe-name"
                class="w-full border-gray-600 text-gray-700 outline-1 outline pl-1 mt-1"
                v-model="recipeName"
              />
            </div>
            <div>
              <label
                for="recipe-type"
                class="block text-sm font-medium text-gray-700"
                >Recipe Type</label
              >
              <div class="mt-1">
                <select
                  id="recipe-type"
                  name="recipe-type"
                  class="block w-full shadow-sm outline outline-1"
                  v-model="recipeType"
                >
                  <option value="meal">Meal</option>
                  <option value="beverage">Beverage</option>
                </select>
              </div>
            </div>
          </form>
        </div>
        <div class="bg-gray-50 px-6 py-3 flex flex-row-reverse">
          <button
            type="button"
            class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:ml-3 sm:w-auto sm:text-sm"
            @click="createNewRecipe()"
          >
            Save
          </button>
          <button
            type="button"
            class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm"
            @click="$emit('close')"
          >
            Cancel
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "AddRecipeDialog",
  data() {
    return {
      recipeName: "",
      recipeType: "",
    };
  },
  methods: {
    async createNewRecipe() {
      try {
        const token = localStorage.getItem("access_token");
        const response = await axios.post(
          "http://localhost:5000/api/recipes",
          {
            name: this.recipeName,
            type: this.recipeType,
          },
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );
        console.log(response.data); // Do something with the response data, if needed
        this.$emit("close");
        this.$emit("recipeAdded", response.data);
      } catch (error) {
        console.error(error); // Handle any errors
      }
    },
  },
};
</script>

<style scoped></style>
