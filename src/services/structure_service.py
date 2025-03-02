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