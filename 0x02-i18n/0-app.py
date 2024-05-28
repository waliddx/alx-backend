#!/usr/bin/env python3

"importing flask"

from flask import Flask, render_template

"creating the route app"

app = Flask(__name__)

"""adding simple route that
    lead to the index html file located
        in templates by using render_temlpate"""

@app.route("/")
def home():
    return render_template("0-index.html")

"app runner"
if __name__ == "__main__":
    app.run(debug=True)
