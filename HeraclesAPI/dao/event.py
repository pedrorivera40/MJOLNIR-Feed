# from firebase import firebase
import os
CURRENT = os.path.dirname(os.path.abspath(__file__))
PARENT = os.path.dirname(CURRENT)
from config.dbconfig import fb_config
# firebase = Firebase(fb_config)
# rtdb = firebase.database()
# storage = firebase.storage()



# if __name__ == '__main__':
#     print(rtdb.v1.get())