<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-900">
    <form class="bg-gray-800 text-white p-8 rounded-lg w-96" novalidate @submit.prevent="register">
      <h1 class="mb-6 text-2xl">Create a New Account</h1>

      <div class="mb-4">
        <label for="email" class="block mb-1">Email:</label>
        <input
          type="email"
          v-model="email"
          id="email"
          name="email"
          required
          class="w-full px-4 py-2 bg-gray-700 rounded-full text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
          :class="{ 'ring-2 ring-red-500': !valid.email }"
        />
        <div v-if="!valid.email" class="text-red-500 text-xs mt-1">Please enter a valid email.</div>
      </div>

      <div class="mb-4">
        <label for="password" class="block mb-1">Password:</label>
        <input
          type="password"
          v-model="password"
          id="password"
          name="password"
          required
          class="w-full px-4 py-2 bg-gray-700 rounded-full text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
          :class="{ 'ring-2 ring-red-500': !valid.password }"
        />
        <div v-if="!valid.password" class="text-red-500 text-xs mt-1">Please enter a password.</div>
      </div>

      <div class="mb-4">
        <label for="confirm-password" class="block mb-1">Confirm Password:</label>
        <input
          type="password"
          v-model="confirmPassword"
          id="confirm-password"
          name="confirm-password"
          required
          class="w-full px-4 py-2 bg-gray-700 rounded-full text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
          :class="{ 'ring-2 ring-red-500': !valid.confirmPassword }"
        />
        <div v-if="!valid.confirmPassword" class="text-red-500 text-xs mt-1">Please confirm your password.</div>
      </div>

      <div class="alert alert-danger mb-4" role="alert" v-if="passwordsDoNotMatch">
        Passwords do not match!
      </div>

      <button
        class="w-full py-2 text-center bg-blue-500 hover:bg-blue-600 rounded-full text-white font-semibold"
        type="submit"
        @click.prevent="register"
      >
        Register
      </button>
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
    async register() {if (!this.validateForm()) {
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
