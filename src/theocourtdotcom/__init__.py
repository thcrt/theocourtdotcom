import flask as f
from flask_vite import Vite


def create_app() -> f.app:
    app = f.Flask(__name__)
    vite = Vite()
    vite.init_app(app)
    app.config["VITE_AUTO_INSERT"] = True

    @app.route("/")
    def index() -> str:
        return f.render_template("index.j2")

    @app.route("/quote")
    def quote() -> str:
        return f.render_template("quote.j2")

    return app
