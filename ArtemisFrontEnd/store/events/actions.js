export default {
  async getAllEvents({commit}){
    try {
      const response = await this.$axios.get('events/') //returns the desired data as jason
      //Calls SET_EVENTS mutation from mutation.js
      commit("SET_EVENTS", response.data) //use .data to extract the actual data from the request. Verify response json to make sure of the structure.
      // console.log(response.data)
    } catch (error) {
      console.log("Trouble fetching events.", error)
    }
  },
  async getEventByID({commit},eid){
    try {
      const response = await this.$axios.get('events/post-id-'+eid+'/')
      commit("SET_SINGLE_EVENT",response.data)
    }catch(error){
      console.log("Trouble fetching event by id. " + error)
    }
  },
  async postComment({commit},commentJSON){
    try {
     
      console.log(commentJSON)
      const response = await this.$axios.post('events/post-id-'+commentJSON.eid+'/comments/',commentJSON) 
      
    }catch(error){
      console.log("Trouble posting a comment. " + error)
    }
  },
}