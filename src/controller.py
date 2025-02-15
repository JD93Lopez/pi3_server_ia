from ai.ai_model import cards
from json_extract.json_extract import extract_json
import json

def get_cards_controller(topic_info):
    if not topic_info:
        topic_info = "Responde un array vacio porque el usuario no ha introducido información del tema, Número de tarjetas: 0"

    card_number = parse_card_number(topic_info)

    resCards = {"tarjetas": []}

    while len(resCards.get("tarjetas")) != card_number:
        resCards = {}
        while not resCards:
            resCards = extract_json(cards(topic_info))
        
        if len(resCards.get("tarjetas")) < card_number:
            continue
        elif len(resCards.get("tarjetas")) > card_number:
            resCards["tarjetas"] = resCards.get("tarjetas")[:card_number]
    
    return resCards

def get_cards_string_controller(topic_info):
    return json.dumps(get_cards_controller(topic_info), ensure_ascii=False, indent=4)


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
            return None
    else:
        print("Delimiter 'Número de tarjetas:' not found in the input string.")
        return None