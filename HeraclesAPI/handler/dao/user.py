from config.dbconfig import fb_config
from firebase import Firebase


''' 
    Data Access Object implementation for the MJOLNIR-Feed prototype.
    This class includes a set of methods to perform CRUD operations over
    the Firebase RTDB instance regarding Users information.
    @author pedrorivera40
'''


class UserDAO:

    def __init__(self):
        self.rtdb = Firebase(fb_config).database()

    # Insert a new user given its username and user_data in a single dictionary object.
    def add_user(self, user_info):
        return self.rtdb.child("v1").child("profiles").child(user_info['username']).set(user_info['user_data'])

    # Obtain all the information regarding a user given its username.
    def get_user(self, username):
        return self.rtdb.child("v1").child("profiles").child(username).get().val()

    # Obtain the hash information of a user
    def get_user_hash(self, username):
        return self.rtdb.child("v1").child("profiles").child(username).child("hash").get().val()


if __name__ == '__main__':
    user_dao = UserDAO()

    # Just getting a user for quick testing.
    print(user_dao.get_user("user-1"))

    # Inserting a dummy user.
    dummy_user = {
        'username': 'IT\'S ME',
        'user_data': {
            'hash': 'TIMON&PUMBA',
            'image-url': 'www.myimg.com',
            'name': 'Fulgencio del Campo',
        },
    }

    print(user_dao.add_user(dummy_user))
