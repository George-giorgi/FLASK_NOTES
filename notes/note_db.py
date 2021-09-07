from flask import Blueprint ,  request ,jsonify, redirect
from Database.reg_db import Note_Db

bp_todo_db = Blueprint("notes", __name__, url_prefix="/")


@bp_todo_db.route("/note", methods = ["GET", "PUT", "DELETE", "POST"])
def todo_db():

    if request.method == "GET":
        send_data = []
        user_email = request.args["user"]
        data = Note_Db(user_email, None,None,None).get_all()
        for i in data:
            ins_data ={
               "email": i[0],
               "content": i[1],
               "time": i[2],
               "important": i[3]
            }
            send_data.append(ins_data)
        return jsonify(send_data)  
    elif request.method =="POST":
        
        user_email =  request.json["user_email"]
        note =  request.json["note"]
        insert_time =  request.json["insert_time"]
        important = request.json["important"]
        
        Note_Db(user_email, note, insert_time,important).add_note()
       
        return "add note sucsess"
    elif request.method =="PUT":
        print(request.json)
        user_email = request.json["user"]
        new_time = request.json["time"]
        old_time = request.json["old_time"]
        important = request.json["important"]
        polimorfizm =  request.json["polimorfizm"]
        content = request.json["content"]
        
        Note_Db(user_email, content, new_time , important ).update_inp_cont(old_time, user_email,polimorfizm )
       
        return "update"
    elif request.method =="DELETE":
       
        time = request.json["time"]
        user = request.json["user"]
        Note_Db(user,  None, time , None ).del_note()
        
        
        return "from delete"


