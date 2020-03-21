from flask import jsonify
from handler.dao.user import UserDAO
import json
import bcrypt
import jwt
import datetime



### BCrypt Authentication Related Functions

#This function iterates over a list of usernames and
#returns true if a matching username is found.
def usernameExists(username):
    user = UserDAO().get_user(username)
    if user != None:
        return True
    else:
        return False


#Uses BCrypt hashing algorithm to hash a password given with 
#the amount of rounds specified in the gensalt() method
#and returns the hash of the password.
def createHash(password):
    utfPasswd = password.encode('utf-8')
    salt = bcrypt.gensalt(rounds=10)#10 rounds for now
    hash = bcrypt.hashpw(utfPasswd,salt)    
    return hash


#Register a new user with the information given in JSON format
def registerUser(json):

    user = UserDAO().addUser(json)
    if user == None:
        return jsonify(Error = "Error with inserting a new user."),403
    return jsonify(Success = "User created in RTDB."),201
    


#Verifies the password given with the password stored in the database
#for an existing user.
def verifyHash(username,password):
    #hardcoding the user to be evaluated
    hash = UserDAO().get_user_hash(username)
    if hash == None:
        return False        
    elif bcrypt.checkpw(password,hash.encode('utf-8')):
        return True
    else:
        return False
       

### JWT Token Related Functions ###


#Generates a new JWT token for the user with the secret key given and returns it.
def generateToken(username,key):
    #Create a JWT token
    token = jwt.encode({'user' : username, 'exp' : datetime.datetime.utcnow()+datetime.timedelta(minutes=3)},key)
    return  jsonify({'token' : token.decode('UTF-8')})   


#Verifies a token with the key given.   
def verifyToken(token,key):
    try:
        jwt.decode(token,key),403
        return True
    except:
        return False

