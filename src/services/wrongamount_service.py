from utils.flashcard_utils import parse_card_number, replace_card_number
from services.card_badinput_service import bad_input_controller, is_bad_input_res

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