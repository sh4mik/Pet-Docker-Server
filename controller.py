from flask import Flask, render_template
from flask import request
import logging

app = Flask(__name__)
dct = {}

@app.route('/storage/<filename>', methods=['GET', 'PUT', 'DELETE'])
def upload_file(filename):
    if request.method == 'PUT':
        dct['/storage/' + filename] = request.data
        return request.data, 201
    if request.method == 'GET':
        res = dct.get('/storage/' + filename)
        if (res == None):
            return "something", 404
        else:
            return dct['/storage/' + filename], 200
    if request.method == 'DELETE':
        try:
            res = dct.pop('/storage/' + filename)
            return 'file deleted', 204
        except KeyError:
            return 'file not found', 404

if __name__ == "__main__":
    app.debug = True
    app.run(port=8080)