<template>
  <v-container>
    <v-row>
      <v-col>
        <h1 class="display-1" v-if="isLoading">Feed for Event:{{eventName}}</h1>
        <h1 class="display-1" v-else> Loading </h1>        
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

    <v-timeline v-if="isLoading">
      <v-timeline-item
        v-for="comment in comments"
        :key="comment.id"
        large
      >
        <template v-slot:icon>
          <v-avatar color="blue">
            <v-icon dark> mdi-account-circle</v-icon>           
          </v-avatar>
        </template>
        <template v-slot:opposite>
          <span>{{comment.user}}</span>
        </template>
        <v-card class="elevation-2">
          <v-card-title class="headline">Commented</v-card-title>
          <v-card-text> {{comment.text}} </v-card-text>        
        </v-card>
      </v-timeline-item>
    </v-timeline>
  </v-container>
</template>

<script>

import {rtdb} from '../../../services/firebaseInit'
import { mapGetters,mapActions } from 'vuex'

export default {  
    data(){
        return{      
            eventName:String,
            textInput:"",            
            comments:[],
                   
        }
    }, 
    created(){
       this.getEventByID(this.$route.params.id),
       this.fetchComments(),      
       this.eventName = ""
       
    },
    computed:{
        
        ...mapGetters({
          event:'events/event',
          user:'/users/user'
        }),        
    },  
    watch:{
        comments:'fetchComments'//Has a problem of duplicating because of the for loop
    },   

    methods: {
        async fetchComments(){
            const db = rtdb()
            try{                
                const commentSnapshot =await db.ref('/v1/posts/comments/post-id-'+this.$route.params.id).once('value')
                this.comments = []
                this.eventName = this.event.title
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
          const commentJSON = {eid:this.$route.params.id,text:this.textInput,user:this.user.username}//THis is expecting the state to have a user.
          
          console.log(commentJSON)
          this.postComment(commentJSON)
          this.textInput = ""
        },
        isLoading(){                            
          return !!this.event
        }        
        
    }
 
    
}
</script>
