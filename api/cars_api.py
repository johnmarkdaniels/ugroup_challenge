from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

import sqlite3
from flask import g

DATABASE = '../database/cars.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

# def index():
#     print('index function')
#     cur = get_db().cursor()

def test_func():
    print('Hello, I am confirming this works')

@app.route('/')
def index():
    cur = get_db().cursor()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

  
################################################################
### SQLAlchemy VERSION

# app = Flask(__name__)
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLITE_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'cars.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# ma = Marshmallow(app)


# class store(db.Model):
#     store = db.Column(db.String(80), primary_key=True)
#     store_id = db.Column(db.String(120), unique=True)

#     def __init__(self, store, store_id):
#         self.store = store
#         self.store_id = store_id


# class StoreSchema(ma.Schema):
#     class Meta:
#         # Fields to expose
#         fields = ('Store', 'Store_ID')


# store_schema = StoreSchema()
# store_schemas = StoreSchema(many=True)
################################################################

# endpoint to create new store

# endpoint to read store(s)

# SQLite VERSION
@app.route('/stores/')
def test_func():
    print('Hello, I am confirming this works')

test_func()

# for store in query_db('select * from Stores_Table limit 5'):
#     print store['Store'], 'has the Store_ID', store['Store_ID']


###############################
# SQLAlchemy VERSION
# # @app.route("/store", methods=["GET"])
# def get_store():
#     all_stores = store.query.all()
#     result = store_schema.dump(all_stores)
#     return jsonify(result.data)
################################

# endpoint to update store(s)

# endpoint to delete store(s)



# endpoint to create new VIN

# endpoint to read VIN(s)

# endpoint to update VIN(s)

# endpoint to delete VIN(s)



# endpoint to create new transaction

# endpoint to read transaction(s)

# endpoint to update transaction(s)

# endpoint to delete transaction(s)


if __name__ == '__main__':
    app.run(debug=True)