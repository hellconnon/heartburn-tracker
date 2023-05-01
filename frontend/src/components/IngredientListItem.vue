<template>
  <div class="">
    <div class="w-8 h-8 border border-gray-300 rounded-full flex items-center justify-center"
      @click="isChecked = !isChecked">
      <div v-if="isChecked" class="bg-green-500 w-6 h-6 rounded-full flex items-center justify-center">
        <i class="fas fa-check text-white"></i>
      </div>
    </div>

    <h3>{{ ingredientName }}</h3>
    <ul>
      <li>Fats: {{ fats }}</li>
      <li>Calories: {{ calories }}</li>
      <li>Proteins: {{ proteins }}</li>
      <li>Carbohydrates: {{ carbohydrates }}</li>
    </ul>
  </div>
</template>
  
<script>
export default {
  props: {
    ingredientName: {
      type: String,
      required: true
    },
    fats: {
      type: Number,
      default: 0
    },
    calories: {
      type: Number,
      default: 0
    },
    proteins: {
      type: Number,
      default: 0
    },
    carbohydrates: {
      type: Number,
      default: 0
    }
  },
  data(){
    return {
      isChecked: false
    }
  }
};
</script>
  
<style></style>
  