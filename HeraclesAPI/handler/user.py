from flask import jsonify
from .dao.user import UserDAO

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

    # this function assumes that the username has been validated and exists
    # call usernameExists if necessary
    def getUserHash(self,username):
        dao = UserDAO()
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

