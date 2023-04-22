<template>
    <div class="login d-flex align-items-center justify-content-center vh-100">
        <form class="bg-dark text-white p-5 rounded-5" novalidate @submit.prevent="login">
            <h3 class="mb-4">Login</h3>

            <div class="mb-3">
                <input placeholder="E-Mail" type="email" v-model="email" id="email" name="email" required class="form-control rounded-pill"
                       :class="{ 'is-invalid': !valid.email }">
                <div class="invalid-feedback">Please enter a valid email.</div>
            </div>

            <div class="mb-3">
                <input type="password" placeholder="Password" v-model="password" id="password" name="password" required class="form-control rounded-pill"
                       :class="{ 'is-invalid': !valid.password }">
                <div class="invalid-feedback">Please enter a password.</div>
            </div>
            <button class="btn btn-outline-light" type="submit" @click.prevent="login">Login</button>
            <div class="mt-0">
                <router-link to="/register" class="text-decoration-none text-white">Create an account</router-link>
            </div>

        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            email: '',
            password: '',
            valid: {
                email: true,
                password: true,
                confirmPassword: true,
            },
        }
    },
    methods: {
        validateForm() {
            this.valid.email = this.email.trim() !== "" && /\S+@\S+\.\S+/.test(this.email);
            this.valid.password = this.password.trim() !== "";
            return this.valid.email && this.valid.password;
        },
        async login() {
            if (!this.validateForm()) {
                return;
            }
            try {
                const response = await fetch('http://localhost:5000/api/auth/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        email: this.email,
                        password: this.password
                    })
                })
                const data = await response.json()
                localStorage.setItem('access_token', data.access_token)
                localStorage.setItem('refresh_token', data.refresh_token)
                this.$router.push('/')
            } catch (error) {
                console.error(error)
            }
        }
    }
}
</script>

<style scoped>
</style>
