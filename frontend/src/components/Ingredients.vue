<template>
    <div class="flex">
        <Sidebar />
        <div class="pl-8 pt-4 grid grid-clos-3 gap-4 h-full w-full">
            <div class="cols-span-1">
                <div class="flex items-center justify-between mb-4">

                    <h2 class="sticky text-3xl text-white font-bold">Ingredients</h2>
                    <div class="flex items-center justify-end">
                        <button
                            class="fas fa-plus text-white border rounded-full w-8 h-8 hover:bg-white hover:text-blue-700 mr-2"
                            @click="showAddIngredient = true"></button>
                        <button
                            class="fas fa-filter text-white border rounded-full w-8 h-8 hover:bg-white hover:text-blue-700 mr-2"></button>
                        <button
                            class="fas fa-sort text-white border rounded-full w-8 h-8 hover:bg-white hover:text-blue-700"></button>

                    </div>
                </div>
                <div class="space-y-2">
          <IngredientListItem
            v-for="(ingredient, index) in ingredients"
            :key="index"
            :ingredient-name="ingredient.name"
            :ingredient-count="ingredient.count"
            :ingredient-type="ingredient.type"
            :selected="index === selectedIndex"
            @select="selectingredient(index, ingredient)"
          />
        </div>
            </div>
            <div class="col-span-2 p-4 rounded-3xl text-white">

            </div>
        </div>


    </div>
</template>

<script>
import Sidebar from "./Sidebar.vue"
import IngredientListItem from "./IngredientListItem.vue";

export default {
    name: "Ingredients",
    components: { Sidebar, IngredientListItem },
    data() {
        return {
            showAddIngredient: false,
            selectedIndex: null,
            ingredients: [
                {name: "Test", fats: 1, calories: 2, proteins: 3, carbohydrates: 4},
            ]
        }
    }
}
</script>

<style scoped></style>