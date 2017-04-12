from flask import Blueprint,request,session,jsonify
from flask import *
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
        return render_template('faculty_login.html' , message = "please fill up all the fields in the form")
    faculty=Faculty.query.filter(Faculty.email==email).first()
    if faculty is None or not faculty.check_password(passwd):
        return render_template('faculty_login.html',  message="Invalid Email/Password")
    session['faculty-id']=faculty.id
    return jsonify(success=True , faculty=faculty.to_dict())

@mod_faculty.route('/registerpage',methods=['GET'])
def register():
    return render_template('faculty_regester.html')


@mod_faculty.route('/register',methods=['POST'])
def create_faculty():
    if not request.form['name'] or not request.form['email'] or not request.form['course_id'] or not request.form['course_name'] or not request.form['course_description'] or not request.form['passwd']:
        return render_template('faculty_regester.html' , message = "please fill up all the fields")
    try:
        name = request.form['name']
        email = request.form['email']
        course_id = request.form['course_id']
        course_name = request.form['course_name']
        course_description=request.form['course_description']
        passwd=request.form['passwd']
    except KeyError as e:
        return render_template('faculty_regester.html' , message="please fill up all the fields")
    if '@' not in email:
        return render_template('faculty_regester.html' ,message="Please enter a valid email,email should contain '@'")
    if len(course_id) != 6:
        return render_template('faculty_regester.html' , message= "Please enter valid course_id")
    prof=Faculty(name,email,course_id,course_name,course_description,passwd)
    db.session.add(prof)
    try:
        db.session.commit()
    except IntegrityError as e:
        return render_template('faculty_regester.html',message="This email or course-id already exists. Pls try a new one") 
    return jsonify(success=True)

@mod_faculty.route('/logout',methods=['POST'])
def logout():
    session.pop('faculty_id')
    return render_template('faculty_login.html')


@mod_faculty.route('/getall',methods=['GET'])
def getall():
    fac = Faculty.query.all()
    users = []
    for faculty in fac:
        u = faculty.to_dict()
        users.append(u)
    return jsonify(allfaculty = users)
