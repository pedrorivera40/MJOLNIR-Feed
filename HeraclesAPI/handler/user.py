from flask import jsonify
from .dao.user import UserDAO


 # Inserting a dummy user.
    # dummy_user = {
    #     'username': 'aWEIRDuser',
    #     'user_data': {
    #         'hash': 'TIMON&PUMBA',
    #         'image-url': 'www.myimg.com',
    #         'name': 'Fulgencio del Campo',
    #         'email': 'aweirdemail@mail.com'
    #     },
    # }

    # print(user_dao.add_user(dummy_user))

class UserHandler:
    #====MOVED FROM AUTH========
    #TODO: Check, is there other functionality that should be moved from auth/main to here?
    #This function iterates over a list of usernames and
    #returns true if a matching username is found.
    def usernameExists(self, username):
        user = UserDAO().get_user(username)
        if user != None:
            return True
        else:
            return False
    
    #Verifies the password given with the password stored in the database
    #for an existing user.

    #TODO: Check if it's better to do the bcryp.checkpw here or if should just do a getHash function. If needed, add import
    def verifyHash(self,username,password):
        #hardcoding the user to be evaluated
        dao = UserDAO
        hash = dao.get_user_hash(username)
        if hash == None:
            return False        
        elif bcrypt.checkpw(password,hash.encode('utf-8')):
            return True
        else:
            return False

    def getUserHash(self,username):
        dao = UserDAO()
        user = dao.get_user(username)
        if not user:
            return jsonify(Error="User Not Found"),404
        else:
            return dao.get_user_hash(username)

    #============================

    #POST
    def createUser(self, form):
        dao = UserDAO()
        if len(form['user_data']) != 4:
            return jsonify(Error="Malformed post request"), 400
        else:
            #TODO: check, do we validate username here? 
            username = form['username']
            #TODO: Check, should hash be created here?
            user_hash = form['user_data']['hash']
            image_url = form['user_data']['image-url']
            name = form['user_data']['name']
            email = form['user_data']['email']
            # assuming ALL fields to be obligatory

            #check if username exists
            if self.usernameExists(username): 
                return jsonify(Error = "Username already exists."),409
            else:
                if username and user_hash and image_url and name and email:
                    result = dao.add_user(form)
                    return jsonify(result)
                else: 
                    return jsonify(Error="Unexpected attributes in post request"), 400

    def getUser(self,username):
        dao = UserDAO()
        user = dao.get_user(username)
        if not user:
            return jsonify(Error="User Not Found"),404
        else:
            return jsonify(user)
    
    def getUserByEmail(self,email):
        dao = UserDAO()
        user = dao.get_account_by_email(email)
        if not user:
            return jsonify(Error="User Not Found"),404
        else:
            return jsonify(user)

