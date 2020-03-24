export default {
  async nameofFucntion({commit}, someVariable){
    try {
      const response = await axios.get(`/route/to/api/call/${someVariable}`) //returns the desired data as jason
      commit("NAME_OF_MUTATION", response.data) //use .data to extract the actual data from the request
    } catch (error) {
      console.log("Log appropriate Error", error)
    }
  }
}