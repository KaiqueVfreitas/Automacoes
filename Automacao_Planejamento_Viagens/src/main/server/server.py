from flask import Flask
from src.main.routes.routes_viagens import viagens_routes_blueprint

app = Flask(__name__)

app.register_blueprint(viagens_routes_blueprint)
