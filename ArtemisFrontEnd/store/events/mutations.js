//Mutations are how you modify the state of the app.
export default {
  NAME_OF_MUTATION: (state, someData) => (state.someStateVar = someData),
  SET_EVNETS: (state, eventsData) => (state.events = eventsData),
}