from flask import Flask, request, jsonify, make_response
import jwt
import json
import datetime
import bcrypt
import os
from auth import usernameExists, registerUser, createHash, verifyHash, generateToken, verifyToken
from functools import wraps
from handler.user import UserHandler
from handler.event import EventHandler


app = Flask(__name__)
app.config['SECRET_KEY'] = 'doom is eternal'

# Verifies that the user accessing a rout has a token and is valid.


def token_check(func):
    @wraps(func)
    def decorated():

        token = request.headers.get('token')

        if not token:
            return jsonify(Error='Token is missing'), 403
        response = verifyToken(token, app.config['SECRET_KEY'])
        if response == False:
            return jsonify(Error="Token is invalid"), 403
        else:
            pass
        return func()
    return decorated


# Hello world route...
@app.route("/login/", methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.json["username"]
        handler = UserHandler()

        # Return error if user does not exist in the system.
        if not handler.usernameExists(username):
            return jsonify(Error="User does not exist, create a new user."), 404

        # Validate user credentials.
        utfPasswd = request.json["password"].encode('utf-8')
        hash = handler.getUserHash(username)

        if verifyHash(hash, utfPasswd):
            return generateToken(username, app.config['SECRET_KEY'])

        return jsonify(Error="Password does not match, please try again."), 409

    return jsonify(Error="HTTP method not allowed")


@app.route("/events/", methods=['GET', 'POST'])
@token_check
def events_feed():
    handler = EventHandler()

    if request.method == 'GET':
        return handler.getAllEvents()

    if request.method == 'POST':
        return handler.insertEvent(request.get_json())

    return jsonify(Error="HTTP method not allowed")


@app.route("/events/<string:event_id>/", methods=['GET', 'PUT', 'DELETE'])
@token_check
def event_view(event_id):
    handler = EventHandler()

    if request.method == 'GET':
        return handler.getEventByID(event_id)

    if request.method == 'PUT':
        return handler.updateEvent(event_id, request.get_json())

    if request.method == 'DELETE':
        return handler.removeEvent(event_id)

    return jsonify(Error="HTTP method not allowed")


@app.route("/events/<string:event_id>/comments/", methods=['POST'])
@token_check
def comment_post(event_id):
    if request.method == 'POST':
        return EventHandler().addComment(event_id, request.get_json())
    return jsonify(Error="HTTP method not allowed")


@app.route("/events/<string:event_id>/comments/<string:comment_id>/", methods=['PUT'])
@token_check
def comment_edit(event_id, comment_id):
    if request.method == 'PUT':
        return EventHandler().updateComment(event_id, comment_id, request.get_json())

    return jsonify(Error="HTTP method not allowed")


# TODO -> Verify if we can use request.get_json() here...
@app.route("/register/", methods=['POST'])
def createUser():
    if request.method == 'POST':
        username = request.json["username"]
        password = request.json["password"]
        imageURL = request.json["image-url"]
        name = request.json["name"]
        email = request.json["email"]
        handler = UserHandler()

        hash = createHash(password)
        userDict = {}
        userDict["username"] = username
        userDict["user_data"] = {"hash": hash.decode(
            'utf-8'), "image-url": imageURL, "name": name, "email": email}
        return handler.createUser(userDict)

    return jsonify(Error="HTTP method not allowed")


# Launch app.
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
