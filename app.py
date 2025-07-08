import flask
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def saludo():
    print(json.dump({f'message''¡Hola,Fiama!'}))

if __name__ == '__main__':
    app.run(debug=True)