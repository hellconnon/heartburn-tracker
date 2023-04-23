<template>
    <li>
        <router-link :to="to"
                     class="p-4 flex items-center justify-center bg-gray-700 text-white rounded-md hover:bg-gray-600 focus:outline-none h-10"
                     :class="isOpen ? 'w-30' : 'w-10'"
                     v-tooltip="{content: text}">
            <i :class="icon"></i>
            <span class="ml-2" v-if="isOpen">{{ text }}</span>

        </router-link>
    </li>
</template>

<script>
export default {
    name: "NavLink",
    props: {
        to: {
            type: String,
            required: true
        },
        icon: {
            type: String,
            required: true
        },
        text: {
            type: String,
            required: true
        },
        isOpen: {
            type: Boolean,
            required: true
        }
    }
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.2s;
}

.fade-enter,
.fade-leave-to {
    opacity: 0;
}
</style>