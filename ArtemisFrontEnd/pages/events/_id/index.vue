<template>
  <v-container>
    <v-row>
      <v-col>
        <h1 class="display-1">Feed for Event:{{eventName}}</h1>        
      </v-col>
    </v-row>
    <v-timeline>
      <v-timeline-item
        v-for="comment in comments"
        :key="comment"
        large
      >
        <template v-slot:icon>
          <v-avatar>
            <img src="http://i.pravatar.cc/64">
          </v-avatar>
        </template>
        <template v-slot:opposite>
          <span>{{comment.user}}</span>
        </template>
        <v-card class="elevation-2">
          <v-card-title class="headline">{{comment.key}}</v-card-title>
          <v-card-text> {{comment.text}} </v-card-text>        
        </v-card>
      </v-timeline-item>
    </v-timeline>
  </v-container>
</template>

<script>
import EventCard from '../../../components/EventCard'
import postData from '../../../data/posts.json'
import eventData from '../../../data/events.json'
import {rtdb} from '../../../services/firebaseInit'

export default {
    components:{
        EventCard
    },
    data(){
        return{      
            eventName:String,
            comments:[], 
        }
    }, 
    created(){
       this.fetchComments()
    },
    watch:{
        comments:'fetchComments'//Has a problem of duplicating because of the for loop
    },

    methods: {
        async fetchComments(){
            const db = rtdb()
            try{
                const postSnapshot = await db.ref('/v1/posts/posts-content/post-id-'+this.$route.params.id).once('value')
                //console.log(postsSnapshot.val().title)
                this.eventName = postSnapshot.val().title
                const commentSnapshot = await db.ref('/v1/posts/comments/post-id-'+this.$route.params.id).once('value')
                this.comments = []
                for (const key in commentSnapshot.val()) {
                    if (commentSnapshot.val().hasOwnProperty(key)) {
                        const element = commentSnapshot.val()[key]
                        this.comments.push(element)
                        
                    }
                }
            }catch(error){
              console.log('i give up: (', error)

            }
        }
    }
 
    
}
</script>
