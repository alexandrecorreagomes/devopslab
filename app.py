from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Deploy de aplicação Python com esteira DevOps"