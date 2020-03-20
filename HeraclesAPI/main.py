from flask import Flask, request, jsonify
app = Flask(__name__)

# Hello world route...
@app.route("/Login/")
def hello():
    return "<h1>This is MJOLNIR's login!!</h1>"

@app.route("/Events/", methods = ['GET', 'POST'])
def events_feed():
    return "<h1>This is MJOLNIR's events feed!!</h1>"

@app.route("/Events/<int:event_id>/", methods = ['GET', 'UPDATE', 'DELETE'])
def event_view(event_id):
    return "<h1>This is MJOLNIR's event view for " + event_id + "!</h1>"

# Launch app.
if __name__ == '__main__':
    app.run()