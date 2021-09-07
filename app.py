from flask import Flask, render_template
from auth.register_login_logaut import reg_bp, log_bp, logout_bp
from wheather_rout.w_rout import bp_wheather
from notes.note_db import bp_todo_db

import os
from flask_cors import CORS

app = Flask(__name__, template_folder= "./build", static_folder="./build/static")
CORS(app)
app.register_blueprint(reg_bp)
app.register_blueprint(log_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(bp_wheather)



app.register_blueprint(bp_todo_db)

app.secret_key = os.urandom(16)

@app.route("/", defaults={"path": ""})
@app.route("/<path>")
def index(path):

    return render_template("index.html")

@app.errorhandler(400)
def error500(error):

    return "heyy what happen :D"

if __name__ == "__main__":

    app.run(debug=True)