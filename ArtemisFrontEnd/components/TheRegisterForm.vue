<template>
      <v-card width="400" class="elevation-12 mx-auto">
        <v-toolbar color="primary" dark flat>
          <v-toolbar-title>Login form</v-toolbar-title>
          <v-spacer />
        </v-toolbar>
        <v-card-text>
          <v-form>
            <v-text-field 
              label="Login" 
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
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn 
            color="primary"
            @click="login()"
          >
            Login
          </v-btn>
        </v-card-actions>
      </v-card>
</template>

<script>
export default {
  name: 'TheLoginForm',
  data() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    login(){
      //TODO axios call to login route.
    }
  }
};
</script>

<style>
</style>