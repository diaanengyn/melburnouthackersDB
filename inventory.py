from flask import Flask
import sqlite3
from __main__ import app

@app.route('/test', methods=['GET'])
def test():
    return 'it works!'


# Members API Route
@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}


if __name__ == "__main__":
    app.run(debug=True)
