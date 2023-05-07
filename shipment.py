import sqlite3
import os
from pathlib import Path
from flask import Blueprint
from flask import jsonify, request
from pypika import Query, Table, Field

shipment = Blueprint('shipment', __name__,
                     template_folder='templates')


def get_db_connection():
    THIS_FOLDER = Path(__file__).parent.resolve()
    DATABASE = os.path.join(THIS_FOLDER, "database.db")
    conn = sqlite3.connect(DATABASE)
    # conn.row_factory = sqlite3.Row
    return conn


@shipment.route('/shipment/supplier/<int:company_id>', methods=['GET'])
def get_from_supplier(company_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = f"SELECT * FROM shipment WHERE supplier_id={company_id}"
    rows = cursor.execute(query).fetchall()
    return jsonify({'shipments': rows})


@shipment.route('/shipment/customer/<int:company_id>', methods=['GET'])
def get_from_customer(company_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = f"SELECT * FROM shipment WHERE customer_id={company_id}"
    rows = cursor.execute(query).fetchall()
    rows = [dict(row) for row in rows]
    return jsonify({'shipments': rows})


@shipment.route('/shipment/add', methods=['POST'])
def add_shipment():
    connection = get_db_connection()
    data = request.get_json()
    inventory_table = Table('shipment')
    query = Query.into(inventory_table).insert(None,
                                               data['shipment_name'],
                                               data['supplier_id'],
                                               data['customer_id'],
                                               data['start_time'],
                                               data['status']).get_sql()

    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()
    return jsonify({'message': 'Shipment created'})


@shipment.route('/shipment/update_status/<int:id>', methods=['PUT'])
def update_status(id):
    connection = get_db_connection()
    data = request.get_json()
    query = f"""
        UPDATE shipment 
        SET status = {data["status"]}
        WHERE id = {id};
        """
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()
    return jsonify({'message': 'Shipment updated'})
