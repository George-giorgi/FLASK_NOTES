from flask import Blueprint , request, session
from werkzeug.security import generate_password_hash, check_password_hash
from Database.reg_db import Person , Database
reg_bp = Blueprint("register", __name__, url_prefix="/")
log_bp = Blueprint("login", __name__, url_prefix="/")
logout_bp = Blueprint("logaut", __name__, url_prefix="/")

@reg_bp.route("/register", methods =["POST"])
def register():
   
    name = request.json["name"]
    email = request.json["email"]
    password = request.json["password"] 
    error = None
    if not name:
        error = "please enter name"
        return error
    elif not email:
        error = "please enter email"
        return error
    elif not password:
        error = "please enter password"
        return error
    
    if error is None:
        reg_result =  Person(name,email,generate_password_hash(password)).register()

        return reg_result
    else:
        return error
    
@log_bp.route("/login", methods = ["POST"])
def login():
    email = request.json["email"]
    password = request.json["password"]
    
    try:
        data = Database(email,password).loggin()
        if check_password_hash(data[2], password):
            session["email"] = data[1]
           
            user = {
                "name": data[0],
                "email": data[1]
            }
            return user 
        else: 

            return "password not matches"        
    except:

        return "this email not found"

  
@logout_bp.route("/logaut")
def logaut():
    
    session.clear()
    
    return "logaut"

