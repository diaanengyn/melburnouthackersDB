import sqlite3
import os
from pathlib import Path
from flask import Blueprint
from pypika import Query, Table, Field
from flask import jsonify, request

step = Blueprint('step', __name__,
                 template_folder='templates')


def get_db_connection():
    THIS_FOLDER = Path(__file__).parent.resolve()
    DATABASE = os.path.join(THIS_FOLDER, "database.db")
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@step.route('/step/<int:shipment_id>', methods=['GET'])
def get_steps(shipment_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = f"SELECT * FROM step WHERE shipment_id={shipment_id}"
    rows = cursor.execute(query).fetchall()
    rows = [dict(row) for row in rows]
    return jsonify({'inventory': rows})


@step.route('/step/add', methods=['POST'])
def add_inventory():
    connection = get_db_connection()
    data = request.get_json()
    inventory_table = Table('step')
    query = Query.into(inventory_table).insert(None,
                                               data['shipment_id'],
                                               data['transporter_id'],
                                               data['start_time'],
                                               data['end_time'],
                                               data['status'],
                                               data['start_loc'],
                                               data['end_loc']).get_sql()

    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()
    return jsonify({'message': 'Inventory created'})


@step.route('/step/update_status/<int:id>', methods=['PUT'])
def update_status(id):
    connection = get_db_connection()
    data = request.get_json()
    query = f"""
        UPDATE step 
        SET end_time = {data["end_time"]},
        status = {data['status']}
        WHERE id = {id};
        """
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()
    return jsonify({'message': 'Inventory updated'})
