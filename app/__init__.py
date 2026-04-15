from flask import Flask
from app.routes.partidos import partidos_bp
from app.routes.resultados import resultados_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(partidos_bp)
    app.register_blueprint(resultados_bp)

    return app