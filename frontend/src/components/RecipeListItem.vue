<template>
  <div class="flex px-4 py-2 rounded-lg border items-center text-white hover:bg-slate-800 hover:text-white" 
  :class="{ 'bg-gray-200 text-slate-900 border': selected }"
  @click="selectRecipe"
  >
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