from flask import Blueprint
login = Blueprint('login', __name__)


@login.route("/login")
def login():
  return render_template('login.html')
