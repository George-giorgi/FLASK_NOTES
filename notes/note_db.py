from flask import Blueprint ,  request 
from Database.reg_db import Note_Db

bp_todo_db = Blueprint("notes", __name__, url_prefix="/")


@bp_todo_db.route("/note", methods = ["GET", "PUT", "DELETE", "POST"])
def todo_db():

    if request.method == "GET":
        user_email = request.args["user_email"]
        # am emailis mixedvit wamovigheb bazidan dasarendereblad

        return "get all notes"
    elif request.method =="POST":
        
        user_email =  request.json["user_email"]
        note =  request.json["note"]
        insert_time =  request.json["insert_time"]
        important = request.json["important"]
        
        Note_Db(user_email, note, insert_time,important ).add_note()
       
        return "add note sucsess"
    elif request.method =="PUT":
        # aq unda daavabdato id is mixedvit, xolo redux shi gavyof sabolood gamogzavnistvis
        user_email = request.json["email"]
        note_id = request.json["id"]
        note_content =  request.json["content"]
        print(user_email, note_id, note_content)
        return "update"
    elif request.method =="DELETE":
        print(request.json)
        time = request.json["time"]
        user = request.json["user"]
        Note_Db(user,  None, time , None ).del_note()
        
        
        return "from delete"


