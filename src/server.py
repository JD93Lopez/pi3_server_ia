from flask import Flask, jsonify, request
from flask_cors import CORS
from controller import get_cards_controller, get_cards_string_controller

app = Flask(__name__)

#enable cors
CORS(app)

# Ruta de ejemplo para una API GET 
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

# Ruta POST para calcular el daño de un héroe
@app.route('/api/cards', methods=['POST'])
def post_cards():
    jsonTopicInfo = request.get_json()
    return jsonify(get_cards_controller(jsonTopicInfo.get("topicInfo"))), 200

# Ruta GET para obtener información de las cartas con un parámetro topicInfo
@app.route('/api/cards', methods=['GET'])
def get_cards():
    topic_info = request.args.get('topicInfo')
    return jsonify(get_cards_controller(topic_info)), 200

# Ruta GET para obtener información de las cartas con un parámetro topicInfo
@app.route('/api/cards/string', methods=['GET'])
def get_cards_string():
    topic_info = request.args.get('topicInfo')
    return jsonify(get_cards_string_controller(topic_info)), 200

if __name__ == '__main__':
    # Cambiar la IP y el puerto
    app.run(host='127.0.0.1', port=5000, debug=True)
