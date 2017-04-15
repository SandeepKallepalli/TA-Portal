from flask import *
from sqlalchemy.exc import IntegrityError
from app import db
from .models import *
mod_tachair = Blueprint('tachair', __name__, url_prefix='/tachair')

@mod_tachair.route('/login', methods=['GET'])
def check_login():
    if 'tachair_id' in session:
        user = Tachair.query.filter(Tachair.id == session['tachair_id']).first()
        return render_template('tachair_home.html', user = user)

    return render_template('tachair_login.html' , message = "please login first")



@mod_tachair.route('/login', methods=['POST'])
def login():
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError as e:
        return render_template('tachair_login.html',message = "Please enter all the  fields")
    user = Tachair.query.filter(Tachair.email == email).first()
    if user is None or not user.check_password(password):
        return render_template('tachair_login.html' , message = "Invalid credentials")
    session['tachair_id'] = user.id
    
    return render_template('tachair_home.html' , user = user)


@mod_tachair.route('/logout', methods=['POST'])
def logout():
    session.pop('tachair_id')
    return render_template('tachair_login.html')

@mod_tachair.route('/register' , methods=['POST'])
def regester():
    try:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        user = Tachair(name,email,password)
        db.session.add(user)
        db.session.commit()
        return jsonify(success = True)
    except:
        return jsonify(success = False)
@mod_tachair.route('/getall' , methods=['GET'])
def getall():
    user = Tachair.query.all()
    users = []
    for u in user:
        users.append(u.to_dict())
    return jsonify(success = True, user = users)
