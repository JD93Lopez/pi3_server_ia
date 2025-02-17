from ai.ai_model import cards
from json_extract.json_extract import extract_json
import json

badInputAnswer = {"tarjetas": [{
    "pregunta": "Algo salió mal, intenta cambiar tu tema o explicación",
    "respuesta": "Algo en tu tema o explicación no le gustó a la IA, intenta corregirlo"
}]}

def get_cards_controller(topic_info):
    if not topic_info:
        topic_info = "Número de tarjetas: 0"

    resCards = wrong_amount_controller(topic_info)
    
    return resCards

def wrong_amount_controller(topic_info):

    card_number = parse_card_number(topic_info)
    resCards = {"tarjetas": []}

    cntIncorrectAmount = -1
    while (len(resCards.get("tarjetas")) != card_number) and (cntIncorrectAmount < 3) and (not is_bad_input_res(resCards)):
        cntIncorrectAmount += 1

        resCards = bad_input_controller(topic_info)
        
        if len(resCards.get("tarjetas")) < card_number:
            continue
        elif len(resCards.get("tarjetas")) > card_number:
            resCards["tarjetas"] = resCards.get("tarjetas")[:card_number]
    
    return resCards

def bad_input_controller(topic_info):

    resCards = {}
    cntIncorrectJson = -1
    badInputRes = True

    while (badInputRes) and (cntIncorrectJson < 2):
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
    
def get_cards_string_controller(topic_info):
    return json.dumps(get_cards_controller(topic_info), ensure_ascii=False, indent=4)