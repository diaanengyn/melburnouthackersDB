import sqlite3
import os
from pathlib import Path
from flask import Blueprint
from flask import jsonify, request
from pypika import Query, Table, Field

inventory = Blueprint('inventory', __name__,
                      template_folder='templates')


def get_db_connection():
    THIS_FOLDER = Path(__file__).parent.resolve()
    DATABASE = os.path.join(THIS_FOLDER, "database.db")
    conn = sqlite3.connect(DATABASE)
    # conn.row_factory = sqlite3.Row
    return conn


@inventory.route('/inventory/<int:company_id>', methods=['GET'])
def get_tasks(company_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = f"SELECT * FROM inventory WHERE company_id={company_id}"
    rows = cursor.execute(query).fetchall()
    return jsonify({'inventory': rows})


@inventory.route('/inventory/add', methods=['POST'])
def add_inventory():
    connection = get_db_connection()
    data = request.get_json()
    inventory_table = Table('inventory')
    query = Query.into(inventory_table).insert(None,
                                               data['product_name'],
                                               data['sku'],
                                               data['description'],
                                               data['price'],
                                               data['quantity'],
                                               data['company_id']).get_sql()
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()
    return jsonify({'message': 'Inventory created'})


@inventory.route('/inventory/update_quantity/<int:id>', methods=['PUT'])
def update_quantity(id):
    connection = get_db_connection()
    data = request.get_json()
    query = f"""
        UPDATE inventory 
        SET quantity = {data["quantity"]}
        WHERE id = {id};
        """
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()
    return jsonify({'message': 'Inventory updated'})


if __name__ == '__main__':
    inventory.run(debug=True)
