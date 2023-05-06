from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import Blueprint, render_template, abort
from flask import current_app
import sqlite3

inventory = Blueprint('inventory', __name__,
                      template_folder='templates')
connection = sqlite3.connect("/Users/dakshagrawal/PycharmProjects/flask-server/database.db")


@inventory.route('/inventory/<int:company_id>', methods=['GET'])
def get_tasks(company_id):
    cursor = connection.cursor()
    query = f"SELECT * FROM inventory WHERE company_id={company_id}"
    rows = cursor.execute(query).fetchall()
    return jsonify({'inventory': rows})


@inventory.route('/inventory/add', methods=['POST'])
def add_inventory():
    data = request.get_json()
    query = f"""
    INSERT INTO inventory(
        product_name={data['product_name']},
                         sku={data['sku']},
                         description={data['description']},
                         price={data['price']},
                         quantity={data['quantity']},
                         company_id={data['company_id']}
    )
    """
    cursor = connection.cursor()
    cursor.execute(query)
    return jsonify({'message': 'Inventory created'})


@inventory.route('/inventory/update_quantity/<int:id>', methods=['PUT'])
def update_quantity(id):
    data = request.get_json()
    query = f"""
        UPDATE inventory 
        SET quantity = {data["quantity"]}
        WHERE id = {id};
        """
    cursor = connection.cursor()
    cursor.execute(query)
    return jsonify({'message': 'Inventory updated'})


if __name__ == '__main__':
    inventory.run(debug=True)
