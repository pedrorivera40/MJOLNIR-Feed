<template>
  <v-card class="mx-auto" max-width="400">
    <v-img
      class="white--text align-end"
      height="200px"
      :src="img"
      gradient="to top, rgba(0, 0, 0, 0.6) 0%, transparent 72px"
    >
      
      <v-card-title >{{title}}</v-card-title>
      
    </v-img>

    <v-card-subtitle class="pb-0">{{date}}</v-card-subtitle>

    <v-card-text class="text--primary">
      <div>{{summary}}</div>
    </v-card-text>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="orange" text>Share</v-btn>

      <v-btn color="orange" text>Explore</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props:{
    title: String,
    summary: String,
    date: String,
    img: String,
  }
};
</script>

<style>
</style>