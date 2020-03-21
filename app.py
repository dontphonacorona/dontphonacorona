from flask import Flask, render_template
application = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')


@application.route("/")
def index():
  return render_template('index.html')
  
@application.route("/login")
def login():
  return render_template('login.html')
  
@application.route("/questionnaire")
def questionnaire():
  return render_template('questionnaire.html')


if __name__ == "__main__":
    application.debug = True
    application.run()