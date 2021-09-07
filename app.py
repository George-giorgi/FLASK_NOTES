from flask import Flask
from auth.register_login_logaut import reg_bp, log_bp, logout_bp
from wheather_rout.w_rout import bp_wheather
from notes.note_db import bp_todo_db

import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(reg_bp)
app.register_blueprint(log_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(bp_wheather)


app.register_blueprint(bp_todo_db)

app.secret_key = os.urandom(16)

@app.route("/")
def index():

    return "heloo from index"



if __name__ == "__main__":

    app.run(debug=True)