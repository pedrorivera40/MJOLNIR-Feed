//Mutations are how you modify the state of the app.
export default {
  SET_USER_DATA(state, userData) {
    //Set user data
    state.user = userData

    //Set userdata in local storage. MAY NEED SECURITY FIXES
    localStorage.setItem('user', JSON.stringify(userData))

    //Set axios headers to contain the auth token by editing default axios config.
    axios.default.headers.common['Authorization'] = `Bearer ${userData.token}`
  },
  CLEAR_USER_DATA() {
    //Forces a fresh of the page and effectively clears state and axios header settings
    location.reload()

    //Clear userdata in local storage.
    localStorage.removeItem('user')
  },
}