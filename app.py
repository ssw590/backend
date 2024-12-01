from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def run_prod():
    from waitress import serve

    serve(app, port=8080)


if __name__ == "__main__":
    app.run(port=8080)
