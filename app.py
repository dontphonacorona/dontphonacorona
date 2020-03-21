from flask import Flask, render_template
from routes.index import index
from routes.login import index

application = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')


application.register_blueprint(index)
application.register_blueprint(login)


if __name__ == "__main__":
    application.debug = True
    application.run()