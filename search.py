from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new")
def new_method():
    return render_template("new.html")

@app.route("/methods",methods=["POST"])
def create_method():
    name = request.form["name"]
    description = request.form["description"]
    category = request.form["category"]
    memo = request.form["memo"]

    return f"""
    name: {name}<br>
    description: {description}<br>
    category: {category}<br>
    memo: {memo}
    """

@app.route("/list")
def methods_list():
    import sqlite3

    con = sqlite3.connect("knowledge.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM methods")
    rows = cur.fetchall()

    con.close()

    return str(rows)

if __name__ == "__main__":
    app.run(debug=True)