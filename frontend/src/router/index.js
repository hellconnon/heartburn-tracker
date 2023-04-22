import {createRouter, createWebHistory} from 'vue-router'
import Home from '../components/Home.vue'
import Login from '../components/Login.vue'
import Register from '../components/Register.vue'
import UserImages from "../components/UserImages.vue";
import Recipes from "../components/Recipes.vue";

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/register',
        name: 'Register',
        component: Register
    },
    {
        path: '/user-images',
        name: 'UserImages',
        component: UserImages
    },
    {
        path: '/recipes',
        name: 'Recipes',
        component: Recipes
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes: routes

})

export default router

