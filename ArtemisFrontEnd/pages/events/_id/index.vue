<template>
  <v-container>
    <v-row>
      <v-col>
        <h1 class="display-1">Feed for Event:{{eventName}}</h1>        
      </v-col>
    </v-row>
   <v-card class="mx-auto" max-width="400" max-height="200">
    
    <v-card-title >Comment</v-card-title>
    <v-text-field
              v-model=textInput
              solo
              label="Write your comment here"
              clearable
    ></v-text-field>   


    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn color="blue" @click="addComment()">Submit</v-btn>
      
    </v-card-actions>
  </v-card>

    <v-timeline>
      <v-timeline-item
        v-for="comment in comments"
        :key="comment"
        large
      >
        <template v-slot:icon>
          <v-avatar>
            <img src="">
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

import {rtdb} from '../../../services/firebaseInit'
import { mapActions } from 'vuex'
import {state} from '../../../store/events/state'



export default {  
    data(){
        return{      
            eventName:String,
            textInput:"",            
            comments:[], 
        }
    }, 
    created(){
       this.eventName = this.getEventByID(this.$route.params.id)
       this.fetchComments()
    },
    watch:{
       // comments:'fetchComments'//Has a problem of duplicating because of the for loop
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
        },
        ...mapActions({
          getEventByID : 'events/getEventByID', //Links to event store and looks for getEvenByID action 
          postComment: 'events/postComment'     
        }),
        addComment(){
          console.log(this.textInput)
          const commentJSON = {text: this.textInput,user:"user-1"}
          
          console.log(commentJSON)
          this.postComment(this.$route.params.id,commentJSON)
          this.textInput = ""
        }
        
        
    }
 
    
}
</script>
