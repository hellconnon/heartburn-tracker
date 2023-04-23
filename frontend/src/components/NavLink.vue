<template>
  <router-link :to="to" class="sidebar-icon group">
    <i :class="icon"></i>
    <span class="sidebar-tooltip group-hover:scale-100">{{ text }}</span>
  </router-link>
</template>

<script>
export default {
  name: "NavLink",
  props: {
    to: {
      type: String,
      required: true,
    },
    icon: {
      type: String,
      required: true,
    },
    text: {
      type: String,
      required: true,
    },
    isOpen: {
      type: Boolean,
      required: true,
    },
  },
};
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
