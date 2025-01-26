from flask import Blueprint, jsonify

viagens_routes_blueprint = Blueprint('viagens_routes', __name__)

@viagens_routes_blueprint.route('/viagens', methods=['POST'])
def criar_viagem():
    return jsonify({'Olá': 'Mundo'}), 200

