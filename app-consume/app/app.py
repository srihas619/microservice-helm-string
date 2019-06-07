from flask import Flask
import json
import requests
import os
import pprint

app = Flask(__name__)
URL = os.environ.get('STR_URL')


@app.route('/health')
def return_ok():
    return 'Ok!', 200


@app.route('/')
def reverse_string():
    if URL:

        try:
            string_consumed = requests.get(url=URL)
            json_data = string_consumed.json()
            message = json_data['message']
            
            if message:
                reverse_message = ""
                for i in message:
                    reverse_message = i + reverse_message
                return json.dumps(reverse_message)
            else:
                return json.dumps("No Content")

        except Exception as e:
            return json.dumps("Exception from upstream "+str(e))

    else:
        return json.dumps({"message": "Upstream URL not set"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
