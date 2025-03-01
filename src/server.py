from flask import Flask, jsonify, request
from flask_cors import CORS
from controller import generate_cards_controller, get_cards_from_map
from waitress import serve

app = Flask(__name__)

#enable cors
CORS(app)

# Ruta de ejemplo para una API GET 
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

# Ruta POST para obtener información de las cartas con un parámetro topicInfo
@app.route('/api/cards', methods=['POST'])
def post_cards():
    jsonTopicInfo = request.get_json()
    cards_id = generate_cards_controller(jsonTopicInfo.get("topicInfo"))
    return jsonify({"cards_id":cards_id}), 200

# Ruta GET para obtener información de las cartas con un parámetro topicInfo
@app.route('/api/cards', methods=['GET'])
def get_cards():
    topic_info = request.args.get('topicInfo')
    topic_id = request.args.get('topicId')
    cards_id = generate_cards_controller(topic_id, topic_info)
    return jsonify({"cards_id":cards_id}), 200

# Ruta GET para obtener información de las cartas en string con un parámetro topicInfo
# @app.route('/api/cards/string', methods=['GET'])
# def get_cards_string():
#     topic_info = request.args.get('topicInfo')
#     cards_id = generate_cards_string_controller(topic_info)
#     return jsonify({"cards_id":cards_id}), 200

# Ruta GET para obtener tarjetas por cards_id
@app.route('/api/cards/get', methods=['GET'])
def get_cards_by_id():
    cards_id = request.args.get('cards_id')
    return jsonify(get_cards_from_map(cards_id)), 200

if __name__ == '__main__':
    # Cambiar la IP y el puerto
    app.run(host='127.0.0.1', port=5000, debug=True)
    # print("Server running on http://127.0.0.1:5000/")
    # serve(app, host='127.0.0.1', port=5000, channel_timeout=120, cleanup_interval=120)
