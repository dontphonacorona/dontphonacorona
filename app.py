from flask import Flask, render_template
import flaskr.routes.index
import flaskr.routes.login

application = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')


app.register_blueprint(index)
app.register_blueprint(login)


if __name__ == "__main__":
    application.debug = True
    application.run()