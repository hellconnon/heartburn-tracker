<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">

            <div class="collapse navbar-collapse" id="sidebarNav">
                <div class="sidebar-sticky">
                    <ul class="nav flex-column">
                        <li class="nav-item">
                            <router-link to="/" class="nav-link text-light">
                                <i class="fas fa-home"></i> Home
                            </router-link>
                        </li>
                        <li class="nav-item">
                            <router-link to="/login" class="nav-link text-light">
                                <i class="fas fa-sign-in-alt"></i> Login
                            </router-link>
                        </li>
                        <li class="nav-item">
                            <router-link to="/register" class="nav-link text-light">
                                <i class="fas fa-user-plus"></i> Register
                            </router-link>
                        </li>
                        <li class="nav-item">
                            <router-link to="/user-images" class="nav-link text-light">
                                <i class="fas fa-images"></i> Images
                            </router-link>
                        </li>
                        <li class="nav-item">
                            <router-link to="/recipes" class="nav-link text-light">
                                <i class="fas fa-user-chef"></i> Recipes
                            </router-link>
                        </li>
                        <li>
                            <router-link to="/ingredients" class="nav-link text-light">
                                <i class="fas fa-carrot"></i> Ingredients
                            </router-link>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </div>
</template>

<script>
export default {
    name: "Sidebar",
};
</script>

<style scoped>
.navbar {
    width: 7%;
    height: 100%;
    position: fixed;
    top: 0;
    left: 0;
}

.sidebar-sticky {
    position: sticky;
    top: 56px;
    height: calc(100vh - 56px);
    padding-top: 0.5rem;
    overflow-x: hidden;
    overflow-y: auto;
}
</style>
