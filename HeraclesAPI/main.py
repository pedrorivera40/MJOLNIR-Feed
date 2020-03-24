from flask import Flask, request, jsonify, make_response
import jwt
import json
import datetime
import bcrypt
import os
from auth import usernameExists,registerUser,createHash,verifyHash,generateToken,verifyToken
from functools import wraps
from handler.user import UserHandler
from handler.event import EventHandler


app = Flask(__name__)
app.config['SECRET_KEY'] ='doom is eternal'

#Verifies that the user accessing a rout has a token and is valid.
def token_check(func):
    @wraps(func)
    def decorated(): 

        token = request.headers.get('token') 

        if not token:           
            return jsonify(Error = 'Token is missing'), 403    
        response = verifyToken(token, app.config['SECRET_KEY'])    
        if response == False:
            return jsonify(Error = "Token is invalid"), 403
        else:
            pass  
        return func()
    return decorated



# Hello world route...
@app.route("/login/",methods = ['POST'])
def login():   
    username = request.json["username"]
    handler = UserHandler()
    if handler.usernameExists(username) == False:
        return jsonify(Error = "User does not exist, create a new user."), 404
    else:
        utfPasswd = request.json["password"].encode('utf-8')
        hash = handler.getUserHash(username)   
        matches = verifyHash(hash,utfPasswd)
        if matches:
            
            return generateToken(username,app.config['SECRET_KEY'])
        else:
            return jsonify(Error = "Password does not match, please try again."), 409

@app.route("/events/", methods = ['GET', 'POST'])
@token_check
def events_feed():       
    return jsonify("This is MJOLNIR's events feed!!")

@app.route("/events/<int:event_id>/", methods = ['GET', 'UPDATE', 'DELETE'])
@token_check
def event_view(event_id):
    return jsonify("This is MJOLNIR's event view for " + event_id + '!')

@app.route("/events/<int>:event_id/comments/",methods = ['POST'])
@token_check
def comment_post(event_id):
    return jsonify("This is MJOLNIR's comment insertion for " + event_id + '!')

@app.route("/events/<int>:event_id/comments/<integer>:comment_id/", methods = ['UPDATE'])
@token_check
def comment_edit(event_id,comment_id):
    return jsonify("This is MJOLNIR's comment edit for " + comment_id + '!')

@app.route("/register/", methods = ['POST'])
def createUser():  
    username = request.json["username"]
    password = request.json["password"]
    imageURL = request.json["image-url"]
    name = request.json["name"]
    email = request.json["email"]
    handler = UserHandler()
        
    hash = createHash(password)  
    userDict = {}      
    userDict["username"] = username
    userDict["user_data"] = {"hash": hash.decode('utf-8'),"image-url":imageURL,"name":name,"email":email}
    return handler.createUser(userDict)

# Launch app.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')




