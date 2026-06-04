from flask import Flask, render_template, request,redirect
import sqlite3

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

    con = sqlite3.connect("knowledge.db")
    cur = con.cursor()

    cur.execute("""
    INSERT INTO methods (name, description, category, memo)
    VALUES (?, ?, ?, ?)
    """, (name, description, category, memo))

    con.commit()
    con.close()

    return redirect("/list")


@app.route("/list")
def methods_list():
    import sqlite3

    con = sqlite3.connect("knowledge.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM methods")
    methods = cur.fetchall()

    con.close()

    return render_template("list.html", methods=methods)

@app.route("/methods/<int:id>")
def detail(id):
    con = sqlite3.connect("knowledge.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM methods WHERE id = ?", (id,))
    method = cur.fetchone()

    con.close()

    return render_template("detail.html", method=method)

if __name__ == "__main__":
    app.run(debug=True)