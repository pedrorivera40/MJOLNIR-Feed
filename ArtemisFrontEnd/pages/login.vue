<template>
  <v-app>
    <TheLoginForm />
  </v-app>
</template>


<script>
  import TheLoginForm from '~/components/TheLoginForm'
  export default {
    layout: "unauthenticated",
    props: {
      source: String
    },
    components: {
      TheLoginForm,
    },
    data() {}
  };
</script>

<style>
</style>