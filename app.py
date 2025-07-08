import flask
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def saludo():
    return jsonify({'message': '¡Hola, Fiama!'})

if __name__ == '__main__':
    app.run(debug=True)