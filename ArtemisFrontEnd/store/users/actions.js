export default {
  async register({ commit }, credentials) {
    try {
      const response = await this.$axios.post('register/', credentials) //returns the desired data as jason
      //use .data to extract the actual data from the request. 
      commit("SET_USER_DATA", response.data) // Verify response json to make sure of the structure.
    } catch (error) {
      console.log("Trouble fetching events.", error)
    }
  },
  async login({ commit }, credentials) {
    try {
      const response = await this.$axios.post('login/', credentials) //returns the desired data as jason
      //use .data to extract the actual data from the request. 
      commit("SET_USER_DATA", response.data) //Verify response json to make sure of the structure.
      this.$router.push('/events')
    } catch (error) {
      console.log("Trouble fetching events.", error)
    }
  },
  logout({ commit }) {
    commit("CLEAR_USER_DATA")
  }
}