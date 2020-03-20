from config.dbconfig import fb_config
from firebase import Firebase

firebase = Firebase(fb_config)
rtdb = firebase.database()
storage = firebase.storage()


if __name__ == '__main__':
    # Just checking if it works by doing a simple query...
    print(rtdb.child("v1").child("posts").get().val())
