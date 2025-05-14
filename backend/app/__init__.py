from flask import Flask
from Routes.main_route import main_bp,student_bp

def create_app():
    app = Flask(__name__,
                template_folder='../../client/templates',
                static_folder='../../client/static')

    app.register_blueprint(main_bp)
    app.register_blueprint(student_bp)
    return app