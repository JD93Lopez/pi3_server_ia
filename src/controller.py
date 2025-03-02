import threading
from services.wrongamount_service import wrong_amount_controller
from services.structure_service import validate_data_structure, limpiar_json
from save_file.cardmap_json import save_cards_map_to_json, load_cards_map_from_json

cardsMap = {}
cardsMap = load_cards_map_from_json(cardsMap)

def get_cards_from_map(cards_id):
    global cardsMap
    return cardsMap.get(str(cards_id))

def delete_cards_from_map(cards_id):
    global cardsMap
    popped = cardsMap.pop(str(cards_id), None)
    save_cards_map_to_json(cardsMap)
    return popped

def generate_cards_controller(topic_id, topic_info):

    cardsId = str(topic_id)
    cardsMap[cardsId] = None

    # Define la función que deseas ejecutar en otro hilo
    def add_pattern():
        thread_generate_cards( topic_info, cardsId )#Tarea a ejecutar en otro hilo

    # Crea un hilo
    hilo = threading.Thread(target=add_pattern)

    # Inicia el hilo
    hilo.start()

    return cardsId

def thread_generate_cards(topic_info, cardsId):
    global cardsMap
    
    if not topic_info:
        topic_info = "Número de tarjetas: 0"

    resCards = None
    cntWrongDataStructure = -1
    while (not validate_data_structure(resCards)) and (cntWrongDataStructure < 2):
        cntWrongDataStructure += 1
        resCards = wrong_amount_controller(topic_info)

    cardsMap[cardsId] = limpiar_json(resCards)
    save_cards_map_to_json(cardsMap)
    
# def generate_cards_string_controller(topic_info):
#     return json.dumps(generate_cards_controller(topic_info), ensure_ascii=False, indent=4)