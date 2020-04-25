from flask import Flask
from views.index import index_blueprint
from views.name import name_blueprint

application = Flask(__name__)
application.register_blueprint(index_blueprint)
application.register_blueprint(name_blueprint)

if __name__ == "__main__":
  application.run()


