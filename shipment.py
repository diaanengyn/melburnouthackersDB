import sqlite3
import os
from pathlib import Path
from flask import Blueprint
from flask import jsonify, request

shipment = Blueprint('shipment', __name__,
                     template_folder='templates')


def get_db_connection():
    THIS_FOLDER = Path(__file__).parent.resolve()
    DATABASE = os.path.join(THIS_FOLDER, "database.db")
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@shipment.route('/shipment/supplier/<int:company_id>', methods=['GET'])
def get_from_supplier(company_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = f"SELECT * FROM shipment WHERE supplier_id={company_id}"
    rows = cursor.execute(query).fetchall()
    return jsonify({'shipments': rows})


@shipment.route('/shipment/supplier/<int:company_id>', methods=['GET'])
def get_from_customer(company_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = f"SELECT * FROM shipment WHERE customer_id={company_id}"
    rows = cursor.execute(query).fetchall()
    return jsonify({'shipments': rows})


@shipment.route('/shipment/add', methods=['POST'])
def add_shipment():
    connection = get_db_connection()
    data = request.get_json()
    query = f"""
    INSERT INTO shipment(
        shipment_name={data['shipment_name']},
                         supplier_id={data['supplier_id']},
                         customer_id={data['customer_id']},
                         start_time={data['start_time']},
                         status={data['status']}
    )
    """
    cursor = connection.cursor()
    cursor.execute(query)
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
    return jsonify({'message': 'Shipment updated'})
