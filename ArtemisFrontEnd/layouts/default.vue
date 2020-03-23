<template>
  <v-app>
    <v-app-bar 
      dark 
      color="blue darken-4" 
      app 
      height="56px"
    >
      <v-toolbar-title 
        class="ml-5 display-1"
      >
      <nuxt-link 
        class="appTitle"
        to="/"
      >
        MM2Events
      </nuxt-link>
      </v-toolbar-title>
    </v-app-bar>
    <v-navigation-drawer 
      v-model="drawer" 
      :mini-variant.sync="mini" 
      permanent 
      app
    >
      <v-list-item class="px-2">
        <v-list-item-avatar>
          <v-img src="https://randomuser.me/api/portraits/men/85.jpg"></v-img>
        </v-list-item-avatar>

        <v-list-item-title>John Leider</v-list-item-title>

        <v-btn 
          icon 
          @click.stop="mini = !mini"
        >
          <v-icon>
            mdi-chevron-left
          </v-icon>
        </v-btn>
      </v-list-item>

      <v-divider></v-divider>

      <v-list dense>
        <v-list-item 
          v-for="item in items" 
          :key="item.title" 
          :to="item.to" 
          nuxt
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>
              {{ item.title }}
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-content>
      <v-container>
        <nuxt />
      </v-container>
    </v-content>

    <v-footer 
      :fixed="fixed" 
      app
    >
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      drawer: true,
      fixed: false,
      items: [
        {
          icon: "mdi-apps",
          title: "Feed",
          to: "/feed"
        },
        {
          icon: "mdi-calendar-multiple",
          title: "Events",
          to: "/events"
        },
      ],
      mini: false,
      title: "Vuetify.js"
    };
  }
};
</script>

<style lang="scss" scoped>
  .appTitle{
    text-decoration: none;
    color:whitesmoke,
  }
</style>