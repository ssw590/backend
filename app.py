from flask import Flask, g, request, jsonify
import sqlite3
from flask_cors import CORS

db_path = "shop.db"


def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


app = Flask(__name__)

CORS(app)


@app.route("/")
def search():
    if "db" not in g:
        g.db = sqlite3.connect(db_path)
        g.db.row_factory = dict_factory

    conn: sqlite3.Connection = g.db
    cursor = conn.cursor()

    search_term = request.args.get("search")

    print(search_term)

    # sql injection
    queryString = f"SELECT name, price FROM items WHERE name LIKE '%{search_term}%' AND released = 1;"

    cursor.execute(queryString)

    return jsonify(cursor.fetchall())


@app.teardown_appcontext
def close_db(error):  # type: ignore
    db = g.pop("db", None)
    if db is not None:
        db.close()


def run_prod():
    from waitress import serve

    serve(app, port=8080)


if __name__ == "__main__":
    app.run(port=8080)
