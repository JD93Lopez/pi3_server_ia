from ai.ai_model import cards
from json_extract.json_extract import extract_json
import threading

badInputAnswer = {"tarjetas": [{
    "pregunta": "Algo salió mal, intenta cambiar tu tema o explicación",
    "respuesta": "Algo en tu tema o explicación no le gustó a la IA o es demasiado extenso o complejo, intenta corregirlo o reintentarlo"
}]}

cardsMap = {}

def get_cards_from_map(cards_id):
    global cardsMap
    return cardsMap.get(str(cards_id))

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

def limpiar_json(data):
    json_limpio = {"tarjetas": data["tarjetas"]}
    return json_limpio

def validate_data_structure(data):
    # Verifica que el parámetro es un diccionario
    if not isinstance(data, dict):
        return False
    # Verifica que 'tarjetas' exista y es una lista
    if "tarjetas" not in data or not isinstance(data["tarjetas"], list):
        return False
    # Verifica si la lista de tarjetas está vacía
    if len(data["tarjetas"]) == 0:
        return True
    # Verifica que cada tarjeta tiene la estructura correcta
    for tarjeta in data["tarjetas"]:
        if not isinstance(tarjeta, dict):
            return False
        # Verifica que 'pregunta' y 'respuesta' existen
        if "pregunta" not in tarjeta or "respuesta" not in tarjeta:
            return False
        if not isinstance(tarjeta["pregunta"], str) or not isinstance(tarjeta["respuesta"], str):
            return False
    return True


def wrong_amount_controller(topic_info):

    card_number = parse_card_number(topic_info)
    resCards = {"tarjetas": []}

    cntIncorrectAmount = -1
    while (len(resCards.get("tarjetas")) != card_number) and (cntIncorrectAmount < 2) and (not is_bad_input_res(resCards)):
        cntIncorrectAmount += 1

        resCards = bad_input_controller(topic_info)
        
        if len(resCards.get("tarjetas")) < card_number:
            if(cntIncorrectAmount == 0):
                topic_info = replace_card_number(topic_info, card_number+10)
                continue
            else:
                break
        elif len(resCards.get("tarjetas")) > card_number:
            resCards["tarjetas"] = resCards.get("tarjetas")[:card_number]
    
    return resCards

def bad_input_controller(topic_info):

    resCards = {}
    cntIncorrectJson = -1
    badInputRes = True

    while (badInputRes) and (cntIncorrectJson < 3):
        cntIncorrectJson += 1

        resCards = extract_json(cards(topic_info), badInputAnswer)

        badInputRes = is_bad_input_res(resCards)
    
    return resCards

def is_bad_input_res(resCards):
    if(  resCards.get("tarjetas") and resCards.get("tarjetas")[0] ):
        return (resCards.get("tarjetas")[0].get("pregunta") == badInputAnswer["tarjetas"][0]["pregunta"])
    else:
        return False

def parse_card_number(input_string):
    parts = input_string.split("Número de tarjetas:")
    
    if len(parts) > 1:
        # Extract the number from the second part and strip any whitespace
        card_number_str = parts[1].strip()
        
        # Try to convert the extracted string to an integer
        try:
            card_number = int(card_number_str)
            return card_number
        except ValueError:
            print("The number of cards could not be converted to an integer.")
            return 0
    else:
        print("Delimiter 'Número de tarjetas:' not found in the input string.")
        return 0
    
def replace_card_number(input_string, new_number):
    # Dividimos el string en dos partes usando "Número de tarjetas:" como delimitador
    parts = input_string.split("Número de tarjetas:")
    
    if len(parts) > 1:
        # La primera parte queda igual (todo antes de "Número de tarjetas:")
        before_label = parts[0]
        
        # La segunda parte contiene el número actual y cualquier cosa después
        after_label = parts[1]
        
        # Buscamos el primer espacio o caracter no numérico para separar el número actual
        number_end_index = 0
        while number_end_index < len(after_label) and after_label[number_end_index].isdigit():
            number_end_index += 1
        
        # Extraemos el resto del string después del número actual
        rest_of_string = after_label[number_end_index:].lstrip()
        
        # Construimos el nuevo string reemplazando el número
        new_string = f"{before_label}Número de tarjetas: {new_number} {rest_of_string}".strip()
        return new_string
    else:
        # Si no se encuentra la etiqueta, devolvemos el input_string original
        print("Delimiter 'Número de tarjetas:' not found in the input string.")
        return input_string
    
# def generate_cards_string_controller(topic_info):
#     return json.dumps(generate_cards_controller(topic_info), ensure_ascii=False, indent=4)