<template>
  <v-container>
    <v-row>
      <v-col>
        <TheRegisterForm />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import TheRegisterForm from '~/components/TheRegisterForm'
export default {
  layout: 'unauthenticated',
  components: {
    TheRegisterForm,
  },
  data() {
    return {

    }
  }
};
</script>

<style>
</style>