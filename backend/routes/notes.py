from flask import Blueprint

notes_bp = Blueprint("notes", __name__)

# Placeholder route
@notes_bp.route("/", methods=["GET"])
def notes_home():
    return {"msg": "Notes route placeholder"}, 200
