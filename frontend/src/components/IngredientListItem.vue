<template>
  <div
    class="flex px-4 py-2 rounded-lg border items-center text-white"
    @click="isChecked = !isChecked"
  >
    <div
      class="w-8 h-8 border border-gray-300 rounded-full flex items-center justify-center"
    >
      <div
        v-if="isChecked"
        class="bg-green-500 w-6 h-6 rounded-full flex items-center justify-center"
      >
        <i class="fas fa-check text-white"></i>
      </div>
    </div>

    <h3 class="text-xl font-bold ml-6">{{ ingredientName }}</h3>
    <div class="flex space-x-3 ml-auto"> 
      <p>Fats: {{ fats }}</p>
      <p>Calories: {{ calories }}</p>
      <p>Proteins: {{ proteins }}</p>
      <p>Carbohydrates: {{ carbohydrates }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    ingredientName: {
      type: String,
      required: true,
    },
    fats: {
      type: Number,
      default: 0,
    },
    calories: {
      type: Number,
      default: 0,
    },
    proteins: {
      type: Number,
      default: 0,
    },
    carbohydrates: {
      type: Number,
      default: 0,
    },
  },
  data() {
    return {
      isChecked: false,
    };
  },
};
</script>

<style></style>
