from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """{question}"""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.2:3b", base_url="http://127.0.0.1:11434/")

chain = prompt | model

instructions = """
Hola LLama, tu trabajo es que eres un especialista en formato JSON
y un genio en todos los temas,
después de la etiqueta "Información del tema:" encontrarás un título de tema "Título del tema:",
su explicación "Explicación:" y una cantidad de tarjetas "Número de tarjetas:".
Tu misión es proporcionar una respuesta JSON con un array llamado cartas 
con objetos que traen cada uno una pregunta y una respuesta.
con una pregunta y una respuesta para cada tarjeta, la mayor cantidad de "Número de tarjetas:" que
cuente sobre el tema.
Las respuestas deben ser lo más concisas posibles,
y las preguntas deben ser lo más claras posibles, la idea es que el usuario
pueda aprender el tema estudiando las tarjetas que hagas y teniendo en cuenta las especificaciones del usuario
"Explicación:", usa la explicación para hacer preguntas que incluyan el contenido que el usuario te brinda en esta sección.
Debes incluir emojis para que las tarjetas se vean más atractivas.
Es obligatorio que la respuesta sea solo en formato JSON solicitado.
Además la respuesta debe estar en el mismo idioma que el tema y la explicación.
Por último es necesario que hagas las tarjetas solo con el contenido del tema
que el usuario te da en la explicación, no añadas ninguna información extra a menos que no se pueda hacer el número 
de cartas solicitado con la información proporcionada.
En tu proceso de pensamiento asegúrate de que si la respuesta está en español no
mezcles palabras en inglés en las tarjetas.
¡Buena suerte! ¡y gracias por tu ayuda!
"""

# print(chain.invoke({"question": instructions + """Topic Information: Topic Title: JSON
# Explanation: JSON is a lightweight data interchange format that is easy for 
# humans to read and write and easy for machines to parse and generate.
# Number of Cards: 3"""}))

print(chain.invoke({"question": instructions + """Información del tema: 
Título del tema: Las ballenas
Explicación: Las ballenas son mamíferos marinos que 
pertenecen al orden de los cetáceos.
Número de tarjetas: 2
"""}))