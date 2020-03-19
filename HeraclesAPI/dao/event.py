from firebase import firebase
from config.dbconfig import fb_config

firebase = Firebase(fb_config)
rtdb = firebase.database()
storage = firebase.storage()



if __name__ == '__main__':
    print(rtdb.v1.get())