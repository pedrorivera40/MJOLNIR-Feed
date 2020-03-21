from flask import Flask, request, jsonify, make_response
import jwt
import json
import datetime
import bcrypt
import os
from auth import usernameExists,registerUser,createHash,verifyHash,generateToken,verifyToken
from functools import wraps


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
@app.route("/Login",methods = ['POST'])
def login():   
    username = request.json["username"]
    if usernameExists(username) == False:
        return jsonify(Error = "User does not exist, create a new user."), 404
    else:
        utfPasswd = request.json["password"].encode('utf-8')    
        matches = verifyHash(username,utfPasswd)
        if matches:
            
            return generateToken(username,app.config['SECRET_KEY'])
        else:
            return jsonify(Error = "Password does not match, please try again."), 409

@app.route("/Events/", methods = ['GET', 'POST'])
@token_check
def events_feed():       
    return "<h1>This is MJOLNIR's events feed!!</h1>"

@app.route("/Events/<int:event_id>/", methods = ['GET', 'UPDATE', 'DELETE'])
@token_check
def event_view(event_id):
    return "<h1>This is MJOLNIR's event view for " + event_id + "!</h1>"

@app.route("/Events/<int>:event_id/comment/",methods = ['POST'])
@token_check
def comment_post(event_id):
    return "<h1>This is MJOLNIR's comment insertion for " + event_id + "!</h1>"

@app.route("/Events/<int>:event_id/comments/<integer>:comment_id/", methods = ['UPDATE'])
@token_check
def comment_edit(event_id,comment_id):
    return "<h1>This is MJOLNIR's comment edit for " + comment_id + "!</h1>"

@app.route("/Register", methods = ['POST'])
def createUser():
  
    username = request.json["username"]
    password = request.json["password"]
    if usernameExists(username): 
        return jsonify(Error = "Username already exists."),409
    else:
        #modifies the request JSON removing the password key and inserting a hash key.        
        request.json["hash"] = createHash(password)        
        del request.json["password"]
        return registerUser(request.json)

# Launch app.
if __name__ == '__main__':
    app.run()




