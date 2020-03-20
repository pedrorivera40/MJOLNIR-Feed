from flask import Flask, request, jsonify, make_response
import jwt
import json
import datetime
import bcrypt
import os
from auth import usernameExists,registerUser,createHash,verifyHash,generateToken
from functools import wraps


app = Flask(__name__)
app.config['SECRET_KEY'] ='doom is eternal'




# Hello world route...
@app.route("/Login",methods = ['POST'])
def login():
   
    username = request.json["username"]
    if usernameExists(usernameExists) == False:
        return jsonify(Error = "User does not exist, create a new user."), 404
    else:
        utfPasswd = request.json["password"].encode('utf-8')    
        matches = verifyHash(username,utfPasswd)
        if matches:
            
            return "<h1>This is MJOLNIR's login!!</h1>"
        else:
            return 
@app.route("/Events/", methods = ['GET', 'POST'])
def events_feed():
    return "<h1>This is MJOLNIR's events feed!!</h1>"

@app.route("/Events/<int:event_id>/", methods = ['GET', 'UPDATE', 'DELETE'])
def event_view(event_id):
    return "<h1>This is MJOLNIR's event view for " + event_id + "!</h1>"

@app.route("/Events/<int>:event_id/comment/",methods = ['POST'])
def comment_post(event_id):
    return "<h1>This is MJOLNIR's comment insertion for " + event_id + "!</h1>"

@app.route("/Events/<int>:event_id/comments/<integer>:comment_id/", methods = ['UPDATE'])
def comment_edit(event_id,comment_id):
    return "<h1>This is MJOLNIR's comment edit for " + comment_id + "!</h1>"

@app.route("/Register", methods = ['POST'])
def createUser():
  
    username = request.json["username"]
    password = request.json["password"]
    if usernameExists(username): 
        return jsonify(Error = "Username already exists."),409
    else:
        request.json["password"] = createHash(password)#modifies the request JSON exchanging the password with the hash.        
        registerUser(request.json)
        return jsonify(Success="Successfully created a new user."),201
        



# Launch app.
if __name__ == '__main__':
    app.run()




