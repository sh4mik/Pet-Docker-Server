from flask import Flask, render_template
from flask import request
import os

import pymongo
import redis
from repository import MongoRepository
from repository import RedisRepository
from service import Service

import logging

app = Flask(__name__)
dct = {}

@app.route('/storage/<filename>', methods=['PUT'])
def put_file(filename):
    if not request.is_json:
        return "error", 400
    service.put('/storage/' + filename, request.data)
    return request.data, 201

@app.route('/storage/<filename>', methods=['GET'])
def get_file(filename):
    res = service.get('/storage/' + filename)
    if (res == None):
        return "something", 404
    else:
        return res["value"], 200

@app.route('/storage/<filename>', methods=['DELETE'])
def delete_file(filename):
    service.delete('/storage/' + filename)
    return 'file deleted', 204


if __name__ == "__main__":
    print("Hello\nim\nhere")

    redis_host = os.getenv('REDIS_HOST')
    redis_port = int(os.getenv('REDIS_PORT'))
    redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
    cache = RedisRepository(redis_client)
    
    mongo_host = os.getenv('MONGO_HOST')
    mongo_port = int(os.getenv('MONGO_PORT'))
    mongo_client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
    mongo_table = mongo_client.pm_server
    mongo_collection = mongo_table.pm_server
    database = MongoRepository(mongo_collection)

    service = Service(cache, database)

    app.run(host='0.0.0.0', port=8080)