from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new")
def new_method():
    return render_template("new.html")

if __name__ == "__main__":
    app.run(debug=True)