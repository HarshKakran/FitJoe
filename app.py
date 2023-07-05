import json

from flask import Flask, send_from_directory, jsonify, request
from flask_cors import cross_origin, CORS
from flask_restful import Api, Resource, reqparse
from utility import collect_messages

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

system_context = '''
    You are FitJoe. FitJoe is an expert fitness bot trained to \
    provide personalized food suggestions based on users' goals \
    and nutritional requirements. FitJoe will analyze the input \
    provided by the user and generate customized recommendations \
    to help them achieve their desired fitness outcomes. \
    FitJoe prioritizes the user's health and safety, and it is \
    programmed to promote balanced and nutritious eating habits. \
    FitJoe may also offer additional guidance, motivation, and tips \
    to support users in their fitness journey. Now, how can I assist \
    you today?
'''

class ChatHandler(Resource):
    def __init__(self, **kwargs):
        self.context = [{"role": "system",
                        "content": system_context}]

    def get(self):
        print(f'GET 19: {self.context}')
        response = jsonify(context=self.context)
        response.headers.add("Access-Control-Allow-Origin", "*")
        # return {
        #     'context': self.context,
        # }
        return response

    # @cross_origin()
    def post(self):
        rqs = request.json
        print(f'POST Print RQS 30 : {rqs}')
        prompt = rqs.get('prompt')
        context = rqs.get('context')

        print(f'POST 34: {prompt}\n{context}')

        response = jsonify(collect_messages(prompt, context))
        return response


api.add_resource(ChatHandler, '/')

if __name__ == '__main__':
    app.run(debug=True)
