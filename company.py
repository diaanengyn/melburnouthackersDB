from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS 

app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

db = SQLAlchemy (app)
class Company (db.Model): 
    id = db.Column ('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    pw = db.Column(db.String(20))

def __init__(id, name, email, pw): 
    self.id = id 
    self.name = name 
    self.email = email
    self.pw = pw

def __repr__(self): 
    return '<Company %r>' % self.title

@app.route('/company', methods=['GET'])
def get_company(): 
    companies = Company.query.all()
    output = []
    for name in companies: 
        name_data = {}
        name_data['id'] = name.id 
        name_data['name'] = name.name 
        name_data['email'] = name.email 
        name_data['pw'] = name.pw 
    return jsonify ({'companies': output})

@app.route('/company/<int:name_id>', methods=['GET'])
def get_name(name_id): 
    name = Company.query.get_or_404(name_id)
    name_data = {}
    name_data['id'] = name.id 
    name_data['name'] = name.name 
    name_data['email'] = name.email 
    name_data['pw'] = name.pw 

@app.route('/company', methods=['POST'])
def add_name(): 
    data = request.get_json()
    new_name = Company(id=data['id'], name=data['name'], email=data['email'], pw=data['pw'])
    db.session.add(new_name)
    db.session.commit()

    #Create a dictionary with relevant information
    response = {
        'id': new_name.id, 
        'name': new_name.name, 
        'email': new_name.email,
        'pw': new_name.pw
        }
    return jsonify({response})

@app.route('/company/<int:name_id>', methods=['PUT'])
def update_name(name_id): 
    name = Company.query.get_or_404(name_id)
    data = request.get_json()
    name.id = data['id']
    name.name = data['name']
    name.email = data['email']
    db.session.commit()
    return jsonify({'message': 'Information Updated!'})

if __name__ == '__main__': 
    db.create_all()
    app.run(debug=True)

# flask shell
# flsk
