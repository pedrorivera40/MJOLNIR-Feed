<template>
  <v-container>
    <v-row>
      <v-col>
        <h1 class="display-1">{{page_title}}</h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <p>{{page_description}}</p>
      </v-col>
    </v-row>
    <v-row>
      <v-col 
        v-for="member in members" 
        :key='member.name'
        cols="8"
        md="6"
        lg="3"
      >
        <ProfileCard
          :name="member.name"
          :img="member.img"
          :bio="member.bio"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

import {rtdb} from '../../services/firebaseInit'
import ProfileCard from '../../components/ProfileCard'

export default {
  components:{
    ProfileCard
  },

  data(){
    return {
      page_title: "",
      page_description: "",
      members:[],
    }
  },

  methods:{

    updateTitle() {
      const db = rtdb()
      try {
        db.ref("v1/about-us/header").on('value', 
          snapshot => {
            console.log(snapshot.val());
            this.page_title = snapshot.val();
          });
      } catch (error) {
        console.log("CRAP! " + error);
      }
    },

    updateDescription() {
      const db = rtdb()
      try {
        db.ref("v1/about-us/description").on('value', 
          snapshot => {
            console.log(snapshot.val());
            this.page_description = snapshot.val();
          });
      } catch (error) {
        console.log("CRAP! " + error);
      }
    },

    updateMembers() {
      const db = rtdb()
      try {
        db.ref("v1/about-us/team").on('value', 
          snapshot => {
            console.log(snapshot.val());
            this.members = snapshot.val();
          });
      } catch (error) {
        console.log("CRAP! " + error);
      }
    },



  },

  created(){
    // Retrieve info from Firebase RTDB.
    this.updateTitle()
    this.updateDescription()
    this.updateMembers()
  }}

</script>
