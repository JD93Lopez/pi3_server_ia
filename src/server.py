from flask import Flask, jsonify, request
from ai.ai_model import cards
from json_extract.json_extract import extract_json, extract_json_string

app = Flask(__name__)

# Ruta de ejemplo para una API GET 
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

# Ruta POST para calcular el daño de un héroe
@app.route('/api/cards', methods=['POST'])
def post_cards():
    jsonTopicInfo = request.get_json()
    return jsonify(extract_json(cards(jsonTopicInfo.get("topicInfo")))), 201

# Ruta GET para obtener información de las cartas con un parámetro topicInfo
@app.route('/api/cards', methods=['GET'])
def get_cards():
    topic_info = request.args.get('topicInfo')
    return jsonify(extract_json(cards(topic_info))), 201

# Ruta GET para obtener información de las cartas con un parámetro topicInfo
@app.route('/api/cards/string', methods=['GET'])
def get_cards_string():
    topic_info = request.args.get('topicInfo')
    return jsonify(extract_json_string(cards(topic_info))), 201

if __name__ == '__main__':
    # Cambiar la IP y el puerto
    app.run(host='127.0.0.1', port=5000, debug=True)
