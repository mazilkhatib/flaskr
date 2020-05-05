from flask import Flask,jsonify


def create_app(test_config=None):
    a = Flask(__name__)

    @app.route('/')
    def hello():
        return jsonify({'message':'HELLO WORLD'})

    return app
