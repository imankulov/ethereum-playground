from flask import Blueprint

bp = Blueprint(__name__, "root", url_prefix="/")


@bp.route("")
def index():
    return "Hello world"
