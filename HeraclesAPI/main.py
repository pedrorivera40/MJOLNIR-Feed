from flask import Flask, request, jsonify

app = Flask(__name__)

# Hello world route...
@app.route("/")
def hello():
    return "<h1>This is MJOLNIR!</h1>"

# Launch app.
if __name__ == '__main__':
    app.run()