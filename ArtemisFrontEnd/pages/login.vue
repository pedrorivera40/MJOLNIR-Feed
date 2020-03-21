<template>
  <v-container 
    class="fill-height"
    fluid
  >
    <v-row justify="center">
      <v-col>
        <TheLoginForm />
      </v-col>
    </v-row>
  </v-container>
</template>


<script>
import TheLoginForm from "~/components/TheLoginForm";
export default {
  layout: "unauthenticated",
  props: {
    source: String
  },
  components: {
    TheLoginForm
  },
  data() {
    return {

    }
  }
};
</script>

<style>
</style>