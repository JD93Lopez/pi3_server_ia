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