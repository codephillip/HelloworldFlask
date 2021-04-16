from flask import Flask, jsonify, request
import json

app = Flask(__name__)

bookslist = [
    {
        "id": 1,
        "name": "Flask book",
        "author": "Flask owner"
    },
    {
        "id": 2,
        "name": "Art of War",
        "author": "Tsun Tzu"
    }
]


movies = [
    {
        "id": 1,
        "title": "Inception",
        "actor": "Decaprio"
    },
    {
        "id": 2,
        "name": "Xmen",
        "author": "Xmen guys"
    }
]

# decorator
@app.route('/')
def hello_world():
    return 'Hello, World!'


# get resources
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({"books": bookslist})


@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify({"movies": movies})


# add resource
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    bookslist.append(data)
    return jsonify(data)
