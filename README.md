# pi3_server_ia
# Built with Llama
# This proyect is made to work with the help of llama 3.2 model
z
# Para instalar Ollama en linux:

sudo ufw allow 11434/tcp

curl -fsSL https://ollama.com/install.sh | sh

# Para instalar el modelo de IA:

ollama run llama3.2:3b

# Para correr proyecto:
# En la carpeta del repositorio:

python -m venv pi3_server_ia-env

.\pi3_server_ia-env\Scripts\activate

pip install -r requirements.txt

python src/server.py

# Para guardar nuevas dependencias instaladas:

pip freeze > requirements.txt