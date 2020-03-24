import firebase from 'firebase'
import firebaseConfig from './firebaseConfig'


// This avoids errors with 'duplicate' firebase apps. Check if there is one app
// already, if not, intialize it. Otherwise, use the app.
// export default !firebase.apps.length ? firebase.initializeApp(firebaseConfig).database() : firebase.app().database()

export function rtdb(){
  return !firebase.apps.length ? firebase.initializeApp(firebaseConfig).database() : firebase.app().database()
}

export function firestore(){
  return !firebase.apps.length ? firebase.initializeApp(firebaseConfig).firestore() : firebase.app().firestore()
}