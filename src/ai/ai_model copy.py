from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="deepseek-r1:7b", base_url="http://127.0.0.1:11434/")

chain = prompt | model

instructions = """
Hi DeepSeek, your job is that you are an JSON format specialist
and genius in all topics,
after the "Topic Information:" tag you will find a topic title "Topic Title:", 
its explanation "Explanation:" and a number of cards "Number of Cards:".
Your mission is to provide a JSON answer of the shape [{"question":,"answer":},{"question":,"answer":}]
with a question and an answer for each card as many "Number of Cards:" tells 
about the topic.
Answers should be as concise as possible, 
and questions should be as clear as possible, the idea is that user 
can learn the topic studying the cards you make and taking into account user's
specifications "Explanation:", use the explanation to make questions incluiding 
the content that the user gives you in this section.
You should include emojis so the cards look more appealing.
It is mandatory so that the answer is only the requested JSON format.
Also the answer must be in the same language as the topic and explanation.
Finally it is necesary that you make the cards only with the content of the topic
that the user gives you in the explanation, don't add any extra information.
In your thinking process make sure that if the answer is in spanish you don't
mix english words in the cards.
Good luck! and thanks for your help!
"""

# print(chain.invoke({"question": instructions + """Topic Information: Topic Title: JSON
# Explanation: JSON is a lightweight data interchange format that is easy for 
# humans to read and write and easy for machines to parse and generate.
# Number of Cards: 3"""}))

print(chain.invoke({"question": instructions + """Topic Information: 
Topic Title: Las ballenas
Explanation: Las ballenas son mamíferos marinos que 
pertenecen al orden de los cetáceos.
Number of Cards: 2
"""}))