from flask import Flask
from .database import db
from .routes.forms import bp as forms_bp


def create_app(config=None):
    app = Flask(__name__, static_folder='../frontend', template_folder='../templates')
    app.config.setdefault('SQLALCHEMY_DATABASE_URI', 'sqlite:///app.db')
    app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)

    if config:
        app.config.update(config)

    db.init_app(app)

    app.register_blueprint(forms_bp)

    @app.route('/')
    def index():
        return app.send_static_file('index.html')

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
