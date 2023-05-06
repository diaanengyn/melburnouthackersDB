from flask import Flask
from inventory import inventory
import db

app = Flask(__name__)
app.app_context().push()
app.register_blueprint(inventory)

# Members API Route
@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}


if __name__ == "__main__":
    app.run(debug=True)
