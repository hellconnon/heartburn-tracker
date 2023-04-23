<template>
    <div id="app" class="min-h-screen bg-gray-900">
        <router-view />
    </div>
</template>

<script>
import {defineComponent} from "vue";
import Sidebar from "./components/Sidebar.vue";

export default defineComponent({
    components: {Sidebar}
})
</script>

<style scoped>
</style>
