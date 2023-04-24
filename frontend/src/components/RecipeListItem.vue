<template>
  <div class="flex px-4 py-2 rounded-lg border items-center text-white " 
  :class="selected ? 'bg-gray-200 text-slate-800 border' : 'hover:bg-slate-800 hover:text-white'"
  @click="selectRecipe"
  >
      <i v-if="recipeType === 'meal'" class="fas fa-hamburger mr-2"></i>
      <i v-if="recipeType === 'beverage'" class="fas fa-wine-bottle mr-2"></i>
      <h3 class="font-bold">{{ recipeName }}</h3>
      <p class="ml-auto text-lg">{{ recipeCount }}</p>
    </div>
</template>

<script>
export default {
    name: "RecipeListItem",
    methods:{
      selectRecipe(){
        this.$emit("select")
      }
    },
    props: {
    recipeType: {
      type: String,
      required: true
    },
    recipeName: {
      type: String,
      required: true
    },
    recipeCount: {
      type: Number,
      required: true
    },
    selected: {
      type: Boolean,
      required: false,
    }
  }
}
</script>

<style scoped>

</style>