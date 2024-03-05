from flask import Flask
from src.sageMakerStableDiffusion.sgStableDiffusionController import route_blueprint, route_path

app = Flask(__name__)


def bootstrap():
    # create app
    app = Flask(__name__)
    # register modules/blueprints
    app.register_blueprint(route_blueprint, url_prefix=f'/{route_path}')
    # start app
    app.run(port=3000, debug=True)


if __name__ == '__main__':
    bootstrap()
