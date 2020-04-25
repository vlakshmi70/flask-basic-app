from flask import Blueprint, render_template

name_blueprint = Blueprint('name',__name__)

@name_blueprint.route("/name")
def name():
  return "Hello VV!"

