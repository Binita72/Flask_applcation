from flask import Flask, jsonify, request
# Tool for interacting with MongoDB database from Python.
import pymongo
# from pymongo import MongoClient   # pip install pymango
from bson.objectid import ObjectId
from bson.json_util import dumps, loads


app = Flask(__name__)


try:
    client = pymongo.MongoClient(host="localhost",
                                 port=27017,
                                 serverSelectionTimeoutMS=1000)
    db = client.test
    # db = client['user_db']
    collection = db['users']
    client.server_info()  # trigger exception if cannot connect to db

except:
    print("ERROR -  Cannot connect to db")

##################################################################################

# Returning a list of all users with GET method

@app.route('/users', methods=['GET'])
def get_users():
    users = list(collection.find())
    serialized_users = []
    for user in users:
        user['_id'] = str(user['_id'])  # Convert ObjectId to string
        serialized_users.append(user)
    return jsonify(serialized_users), 200


##################################################################################
# Returning the user with the specified ID

@app.route('/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = collection.find_one({'_id': ObjectId(user_id)})
    if user:
        user_json = loads(dumps(user))
        return jsonify(user_json), 200
    else:
        return jsonify({'message': 'User not found'}), 404

##################################################################################
# Creating a new user with the specified data


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = {
        'name': data['name'],
        'email': data['email'],
        'password': data['password']
    }
    result = collection.insert_one(user)
    return jsonify({'message': 'User created', 'id': str(result.inserted_id)}), 201

##################################################################################
# Updating the user with the specified ID with the new data


@app.route('/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = collection.find_one({'_id': ObjectId(user_id)})
    if user:
        updated_user = {
            'name': data['name'],
            'email': data['email'],
            'password': data['password']
        }
        collection.update_one({'_id': ObjectId(user_id)}, {
                              '$set': updated_user})
        return jsonify({'message': 'User updated'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404
##################################################################################
# Deleting the user with the specified ID


@app.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = collection.find_one({'_id': ObjectId(user_id)})
    if user:
        collection.delete_one({'_id': ObjectId(user_id)})
        return jsonify({'message': 'User deleted'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404

##################################################################################


if __name__ == "__main__":
    app.run(port=90, debug=True)
