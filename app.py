from flask import Flask
from inventory import inventory
from shipment import shipment
from step import step
from company import company

app = Flask(__name__)
app.app_context().push()
app.register_blueprint(inventory)
app.register_blueprint(shipment)
app.register_blueprint(step)
app.register_blueprint(company)


# Members API Route
@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}


if __name__ == "__main__":
    app.run(debug=True)
