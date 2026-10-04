# pyright: reportMissingImports=false
from flask import Flask, jsonify
import datetime
import socket 

app = Flask(__name__)


@app.route('/api/v1/details')

def details():
    return jsonify({
        "message": "Hello building the IDP with backstage",
        "status": "success",
        "hostname": socket.gethostname(),
        "time:": datetime.datetime.now().strftime("%Y-%m-%d. %H:%M:%S"),
        "data": {
            "name": "IDP",
            "version": "3.0.0",
            "description": "This is a sample IDP application built with Flask and Backstage."
        }
    })

@app.route('/api/v1/healthz')

def healthz():
    return jsonify({
        "status": "up",
        "hostname": socket.gethostname(),
        "time:": datetime.datetime.now().strftime("%Y-%m-%d. %H:%M:%S")
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')

#
#'/api/v1/details'
#'/api/v1/healthz'

