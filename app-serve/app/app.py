from flask import Flask
import json
import os

app = Flask(__name__)


@app.route('/health')
def return_ok():
    return 'Ok!', 200


@app.route('/')
def return_string():
    return json.dumps({"id": "1","message": "Hello world"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5500)
