import json
import threading
import os

def save_cards_map_to_json(cardsMap):
    """
    Guarda el diccionario cardsMap en un archivo JSON llamado 'cardsMap.json'
    utilizando un hilo separado para no bloquear la ejecución del programa.
    
    :param cardsMap: Diccionario a guardar en el archivo JSON.
    """
    def save_to_file():
        with open("cardsMap.json", "w", encoding="utf-8") as file:
            json.dump(cardsMap, file, ensure_ascii=False, indent=4)
        # print("El mapa se ha guardado correctamente en 'cardsMap.json'.")

    # Crear y ejecutar el hilo para guardar el archivo
    thread = threading.Thread(target=save_to_file)
    thread.start()

def load_cards_map_from_json(cardsMap):
    """
    Carga el diccionario cardsMap desde el archivo JSON 'cardsMap.json'
    solo si el diccionario pasado como parámetro está vacío.
    
    :param cardsMap: Diccionario a verificar y cargar si está vacío.
    :return: El diccionario cargado desde el archivo JSON o un diccionario vacío si no hay archivo o está vacío.
    """
    if not cardsMap:  # Verifica si cardsMap está vacío
        if os.path.exists("cardsMap.json"):  # Verifica si el archivo existe
            try:
                with open("cardsMap.json", "r", encoding="utf-8") as file:
                    loaded_map = json.load(file)
                # print("El mapa se ha cargado correctamente desde 'cardsMap.json'.")
                return loaded_map
            except json.JSONDecodeError:
                print("Error al decodificar el archivo JSON. El archivo podría estar corrupto.")
            except Exception as e:
                print(f"Ocurrió un error al cargar el archivo JSON: {e}")
        else:
            print("El archivo 'cardsMap.json' no existe. No se cargó ningún mapa.")
    return {}  # Retorna un diccionario vacío si no se cargó nada