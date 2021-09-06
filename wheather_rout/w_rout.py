from flask import Flask, Blueprint, jsonify
import mysql.connector as mydb

bp_wheather = Blueprint("wheather", __name__, url_prefix="")

credentials = {
    "host": "localhost",
    "user": "root",
    "database": "REACT_REDUX_FLASK_NOTES",
    "password": "Wagvl1chorchana123"
}

@bp_wheather.route("/wheather")
def wheather():
    send_data = []
    conn = mydb.connect(**credentials)
    cursor = conn.cursor()

    cursor.execute("SELECT * from wheather")

    data = cursor.fetchall()
    for i in data:

        obj_data = {
            "city": i[0],
            "temp": i[1],
            "time": i[2],
            "sky": i[3],
            "id": i[4]
        }
        send_data.append(obj_data)
    conn.close()

   
    return jsonify(send_data)

