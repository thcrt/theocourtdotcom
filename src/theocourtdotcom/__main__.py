from waitress import serve

from theocourtdotcom import create_app

if __name__ == "__main__":
    app = create_app()
    serve(app, host="0.0.0.0", port=8080)
