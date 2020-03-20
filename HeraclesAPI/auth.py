from flask import jsonify
import json
import bcrypt
import jwt



#This function iterates over a list of usernames and
#returns true if a matching username is found.
def usernameExists(username):
    jsonFile = jsonFile = open('mjolnir-feed-export.json')
    jsonObj = json.load(jsonFile)        
    users = jsonObj["v1"]["profiles"]
    if username in users.keys():
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
    
    return


#Verifies the password given with the password stored in the database
#for an existing user.
def verifyHash(username,password):
    #hardcoding the user to be evaluated
    jsonFile = open('mjolnir-feed-export.json')#replace after integrated with db
    jsonObj = json.load(jsonFile)
    profiles = jsonObj["v1"]["profiles"]
    for user in profiles.keys():
        if username == user:
            if bcrypt.checkpw(password,profiles[user]["hash"].encode('utf-8')):
                return True
            else:
                return False
        else:
            return False 

def generateToken():
    return    