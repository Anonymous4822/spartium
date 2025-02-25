from flask import Flask
import os

app = Flask(__name__)

# Lire la variable d'environnement MESSAGE
message = os.getenv("MESSAGE", "Bienvenue dans votre application web minimaliste !")

@app.route("/")
def home():
    return f"<h1>{message}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001)
