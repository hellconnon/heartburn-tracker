<template>
    <div class="register d-flex align-items-center justify-content-center vh-100">
        <form class="bg-dark text-white p-5 rounded" novalidate @submit.prevent="register">
            <h1 class="mb-4">Create a New Account</h1>

            <div class="mb-3">
                <label for="email" class="form-label">Email:</label>
                <input type="email" v-model="email" id="email" name="email" required class="form-control"
                       :class="{ 'is-invalid': !valid.email }">
                <div class="invalid-feedback">Please enter a valid email.</div>
            </div>

            <div class="mb-3">
                <label for="password" class="form-label">Password:</label>
                <input type="password" v-model="password" id="password" name="password" required class="form-control"
                       :class="{ 'is-invalid': !valid.password }">
                <div class="invalid-feedback">Please enter a password.</div>
            </div>

            <div class="mb-3">
                <label for="confirm-password" class="form-label">Confirm Password:</label>
                <input type="password" v-model="confirmPassword" id="confirm-password" name="confirm-password" required
                       class="form-control" :class="{ 'is-invalid': !valid.confirmPassword }">
                <div class="invalid-feedback">Please confirm your password.</div>
            </div>

            <div class="alert alert-danger" role="alert" v-if="passwordsDoNotMatch">
                Passwords do not match!
            </div>

            <button class="btn btn-outline-light" type="submit" @click.prevent="register">Register</button>
        </form>
    </div>
</template>

<script>
export default {
    name: "Register",
    data() {
        return {
            email: "",
            password: "",
            confirmPassword: "",
            passwordsDoNotMatch: false,
            valid: {
                email: true,
                password: true,
                confirmPassword: true,
            },
        };
    },
    methods: {
        validateForm() {
            this.valid.email = this.email.trim() !== "" && /\S+@\S+\.\S+/.test(this.email);
            this.valid.password = this.password.trim() !== "";
            this.valid.confirmPassword = this.confirmPassword.trim() !== "";
            return this.valid.email && this.valid.password && this.valid.confirmPassword;
        },
        async register() {
            if (!this.validateForm()) {
                return;
            }
            if (this.password.trim() === this.confirmPassword.trim()) {
                this.passwordsDoNotMatch = false;
            } else {
                this.passwordsDoNotMatch = true;
                return;
            }
            try {
                const response = await fetch("http://localhost:5000/api/auth/register", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        email: this.email,
                        password: this.password,
                    }),
                });
                const data = await response.json();
                localStorage.setItem("access_token", data.access_token);
                localStorage.setItem("refresh_token", data.refresh_token);
                console.log(data);
                this.$router.push("/");
            } catch (error) {
                console.error(error);
            }
        },
    },
};
</script>

<style scoped>
.register {
    width: 100%;
    max-width: 500px;
}
</style>
