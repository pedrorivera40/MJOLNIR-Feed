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
      <v-btn @click="login()" class="ma-3" to="/register">Register</v-btn>
      <v-btn dark color="blue lighten-1" @click="lol()" class="ma-3">Login</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { rtdb, firestore } from "../services/firebaseInit";
export default {
  name: "TheLoginForm",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    async login() {
      //TODO axios call to login route.
      try {
        const fs = firestore();
        const snapshot = await fs.collection("users").get();
        console.log(snapshot.docs[0]);
      } catch (error) {
        console.log(error);
      }
    },
  }
};
</script>

<style>
</style>