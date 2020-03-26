<template>
  <v-card width="500" class="elevation-12 mx-auto">
    <v-toolbar color="blue accent-3" dark flat>
      <v-toolbar-title>Login</v-toolbar-title>
      <v-spacer />
    </v-toolbar>
    <v-card-text>
      <v-container>
        <v-form>
          <v-text-field
            label="Username"
            name="login"
            prepend-icon="mdi-account"
            type="text"
            v-model="username"
          />

          <v-text-field
            id="password"
            label="Password"
            name="password"
            prepend-icon="mdi-lock"
            append-icon="mdi-eye-off"
            type="password"
            v-model="password"
          />
        </v-form>
      </v-container>
    </v-card-text>
    <v-card-actions>
      <a class="ml-4">Forgot Password?</a>
      <v-spacer />
      <v-btn class="ma-3" to="/register">Register</v-btn>
      <v-btn dark color="blue lighten-1" class="ma-3" @click="login({username: username, password: password})">Login</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { mapActions } from "vuex"

export default {
  name: "TheLoginForm",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    ...mapActions({
      login: 'users/login'
    })
  }
};
</script>

<style>
</style>