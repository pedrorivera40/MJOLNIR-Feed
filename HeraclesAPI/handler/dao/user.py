from config.dbconfig import fb_config
from firebase import Firebase


class UserDAO:

    def __init__(self):
        self.rtdb = Firebase(fb_config).database()

    def add_user(self, user_info):
        return self.rtdb.child("v1").child("profiles").child(user_info['username']).set(user_info['user_date'])

    def get_user(self, username):
        return self.rtdb.child("v1").child("profiles").child(username).child("hash").get().val()


if __name__ == '__main__':
    user_dao = UserDAO()

    # Just getting a user for quick testing.
    print(user_dao.get_user("user-1"))
