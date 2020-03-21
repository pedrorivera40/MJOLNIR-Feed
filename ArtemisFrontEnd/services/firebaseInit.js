import firebase from 'firebase'
import firebaseConfig from './firebaseConfig'


// This avoids errors with 'duplicate' firebase apps. Check if there is one app
// already, if not, intialize it. Otherwise, use the app.
export default !firebase.apps.length ? firebase.initializeApp(firebaseConfig).database() : firebase.app().database()


// let v1 = {
//   events: {
//     one: {
//       title: '',
//       image: '',
//       date: '',
//       text: '',
//       author: '',
//     },
//     two: {
//       title: '',
//       image: '',
//       date: '',
//       text: '',
//       author: '',
//     },
//     three: {
//       title: '',
//       image: '',
//       date: '',
//       text: '',
//       author: '',
//     },
//     four: {
//       title: '',
//       image: '',
//       date: '',
//       text: '',
//       author: '',
//     },

//   },

//   members:{
//     one:{
//       userID3: true,
//       userID5: true,
//     },
//     two:{
//       userID2: true,
//     },
//     three:{
//       userID2: true,
//       userID3: true,
//       userID4: true,
//     },
//     four:{
//       userID1: true,
//       userID5: true,
//     },
//   },

//   messages: {

//   },

//   users: {
//     userID1:{
//       name: '',
//       email: '',
//       image: '',
//       hash: '',
//     },
//     userID2:{
//       name: '',
//       email: '',
//       image: '',
//       hash: '',
//     },
//     userID3:{
//       name: '',
//       email: '',
//       image: '',
//       hash: '',
//     },
//     userID4:{
//       name: '',
//       email: '',
//       image: '',
//       hash: '',
//     },
//     userID5:{
//       name: '',
//       email: '',
//       image: '',
//       hash: '',
//     },
//   }
// }