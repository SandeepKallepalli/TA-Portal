from flask import Blueprint,request,session,jsonify
from sqlalchemy.exc import IntegrityError
from app import db
from .models import Faculty

mod_faculty=Blueprint('faculty',__name__,url_prefix='/faculty')

@mod_faculty.route('/login',methods=['GET'])
def check_login():
    if 'faculty_id' in session:
        faculty=Faculty.query.filter(Faculty.id==session['faculty_id']).first()
        return jsonify(success=True,user=user.to_dict())
    return jsonify(success=False),401

@mod_faculty.route('/login',methods=['POST'])
def login():
    try:
        email = request.form['email']
        passwd = request.form['passwd']
    except KeyError as e:
        return jsonify(success=False,message="%s argument not sent to the request" %e.args),400
    faculty=Faculty.query.filter(Faculty.email==email).first()
    if user is None or not faculty.check_password(passwd):
        return jsonify(uccess=True,message="Invalid Email/Password"),400
    session['faculty-id']=faculty.id
    return jsonify(success=False , faculty=faculty.to_dict())




@mod_faculty.route('/register',methods=['POST'])
def create_faculty():
    try:
        name = request.form['name']
        email = request.form['email']
        course_id = request.form['course_id']
        course_name = request.form['course_name']
        course_description=request.form['course_description']
        passwd=request.form['passwd']
    except KeyError as e:
        return jsonify(success=False,message="%s not sent in to the request", %e.args) , 400
    if '@' not in email:
        return jsonify(success=False,message="Please enter a valid email,email should contain '@'"),400
    prof=Faculty(name,email,course_id,course_name,course_description,passwd)
    db.session.add(prof)
    try:
        db.session.commit()
    except IntegrityError as e:
        return jsonify(success=False,message="This email already exists. Pls try a new one") , 400
    return jsonify(success=True)
@mod_faculty.route('/logout',methods=['POST'])
def logout():
    session.pop('faculty_id')
    return jsonify(success=True)
