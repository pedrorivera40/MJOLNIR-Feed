<template>
  <v-container>
    <v-row>
      <v-col>
        <h1 class="display-1">Upcomming Events</h1>
      </v-col>
    </v-row>
    <v-row>
      <v-col 
        v-for="event in events" 
        :key="event.id"
        cols="12"
        md="6"
        lg="3"
      >
        <EventCard
          :title="event.title"
          :date="event.date"
          :summary="event.summary"
          :img="event.img"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import EventCard from '../../components/EventCard'
import eventsData from '../../data/events.json'
export default {
  components:{
    EventCard
  },
  data(){
    return {
      events:eventsData,
    }
  }


}
</script>

<style>

</style>