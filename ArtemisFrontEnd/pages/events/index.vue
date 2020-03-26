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
import { mapGetters, mapActions } from 'vuex'

export default {
  components:{
    EventCard
  },
  // middleware:['auth'], enable when login is implemented
  data(){
    return {
    }
  },
  methods:{
    ...mapActions({
      getAllEvents: 'events/getAllEvents' //links the events store, looks for getAllEvents action
    })
  }
  ,computed:{
    ...mapGetters({
      events: 'events/events' //maps state.events to events
    })
  },
  created(){
    // TODO: Uncomment once API is ready.
    this.getAllEvents()

    //Pulling events from firebase directly
    // const fs = firestore()
    // fs.collection('events').get()
    // .then(snapshot=>{
    //   snapshot.forEach(doc =>{
    //     const event = {
    //       'author': doc.data().author,
    //       'date': doc.data().date,
    //       'img': doc.data().img,
    //       'last_update': doc.data().last_update,
    //       'summary': doc.data().summary,
    //       'title': doc.data().title
    //     }

    //     this.events.push(event)
    //   })
    // })
  }


}
</script>

<style>

</style>