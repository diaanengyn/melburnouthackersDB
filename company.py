import sqlite3
import os
from pathlib import Path
from flask import Blueprint
from pypika import Query, Table, Field
from flask import jsonify, request

company = Blueprint('company', __name__,
                    template_folder='templates')


def get_db_connection():
    THIS_FOLDER = Path(__file__).parent.resolve()
    DATABASE = os.path.join(THIS_FOLDER, "database.db")
    conn = sqlite3.connect(DATABASE)
    # conn.row_factory = sqlite3.Row
    return conn


@company.route('/company/add', methods=['POST'])
def add_inventory():
    connection = get_db_connection()
    data = request.get_json()
    inventory_table = Table('company')
    query = Query.into(inventory_table).insert(None,
                                               data['name'],
                                               data['email'],
                                               data['password']).get_sql()

    cursor = connection.cursor()
    cursor.execute(query)
    id = cursor.lastrowid
    connection.commit()
    connection.close()
    return jsonify({'message': 'Company created', 'id': id})
