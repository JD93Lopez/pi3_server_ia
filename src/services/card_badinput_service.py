from ai.ai_model import cards
from json_extract.json_extract import extract_json

badInputAnswer = {"tarjetas": [{
    "pregunta": "Algo salió mal, intenta cambiar tu tema o explicación",
    "respuesta": "Algo en tu tema o explicación no le gustó a la IA o es demasiado extenso o complejo, intenta corregirlo o reintentarlo"
}]}

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