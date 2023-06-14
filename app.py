import json

from flask import Flask, send_from_directory, jsonify, request
from flask_restful import Api, Resource, reqparse
from utility import collect_messages

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
api = Api(app)


class ChatHandler(Resource):
    def __init__(self, **kwargs):
        self.context = {}

    def get(self):
        return {
            'context': self.context,
        }

    def post(self):
        # print(type(request.form.get('prompt')))
        prompt = request.form.get('prompt')
        context = list(request.form.get('context'))
        return collect_messages(prompt, context)


api.add_resource(ChatHandler, '/')

if __name__ == '__main__':
    app.run(debug=True)
