import sqlite3
import os
from pathlib import Path
from flask import Blueprint
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
def get_tasks(shipment_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = f"SELECT * FROM step WHERE shipment_id={shipment_id}"
    rows = cursor.execute(query).fetchall()
    return jsonify({'inventory': rows})


@step.route('/step/add', methods=['POST'])
def add_inventory():
    connection = get_db_connection()
    data = request.get_json()
    query = f"""
    INSERT INTO step(
        shipment_id={data['shipment_id']},
                         transporter_id={data['transporter_id']},
                         start_time={data['start_time']},
                         end_time={data['end_time']},
                         status={data['status']}
    )
    """
    cursor = connection.cursor()
    cursor.execute(query)
    return jsonify({'message': 'Inventory created'})


@step.route('/step/update_status/<int:id>', methods=['PUT'])
def update_status(id):
    connection = get_db_connection()
    data = request.get_json()
    query = f"""
        UPDATE step 
        SET quantity = {data["quantity"]},
        status = {data['status']}
        WHERE id = {id};
        """
    cursor = connection.cursor()
    cursor.execute(query)
    return jsonify({'message': 'Inventory updated'})
