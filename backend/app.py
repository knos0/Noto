from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object("config.Config")

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Importing blueprints
from routes.auth import auth_bp
from routes.notes import notes_bp

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(notes_bp, url_prefix="/notes")

if __name__ == "__main__":
    app.run(debug=True)


with app.app_context():
    db.create_all()
