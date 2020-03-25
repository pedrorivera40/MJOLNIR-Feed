export default {
  async getAllEvents({commit}){
    try {
      const response = await this.$axios.get('/events/') //returns the desired data as jason
      //Calls SET_EVENTS mutation from mutation.js
      commit("SET_EVENTS", response.data) //use .data to extract the actual data from the request. Verify response json to make sure of the structure.
    } catch (error) {
      console.log("Trouble fetching events.", error)
    }
  }
}