<template>
  <div class="min-h-screen min-w-screen flex items-center justify-center bg-gray-900">
    <form class="bg-gray-800 text-white p-8 rounded-lg w-96" novalidate @submit.prevent="login">
      <h3 class="mb-6 text-2xl">Login</h3>

      <div class="mb-4">
        <input
          placeholder="E-Mail"
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
        <input
          type="password"
          placeholder="Password"
          v-model="password"
          id="password"
          name="password"
          required
          class="w-full px-4 py-2 bg-gray-700 rounded-full text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
          :class="{ 'ring-2 ring-red-500': !valid.password }"
        />
        <div v-if="!valid.password" class="text-red-500 text-xs mt-1">Please enter a password.</div>
      </div>

      <button
        class="w-full py-2 text-center bg-blue-500 hover:bg-blue-600 rounded-full text-white font-semibold"
        type="submit"
        @click.prevent="login"
      >
        Login
      </button>

      <div class="mt-4 text-center">
        <router-link to="/register" class="text-white hover:text-blue-500">Create an account</router-link>
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
    };
  },
  methods: {
    validateForm() {
      this.valid.email = this.email.trim() !== '' && /\S+@\S+\.\S+/.test(this.email);
      this.valid.password = this.password.trim() !== '';
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
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            email: this.email,
            password: this.password,
          }),
        });
        const data = await response.json();
        localStorage.setItem('access_token', data.access_token);
        localStorage.setItem('refresh_token', data.refresh_token);
        this.$router.push('/');
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>
