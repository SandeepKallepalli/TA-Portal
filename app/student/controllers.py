from flask import *
from sqlalchemy.exc import IntegrityError
from app import db
from .models import Student

mod_student = Blueprint('student', __name__, url_prefix='/student')

@mod_student.route('/login', methods=['GET'])
def check_login():
    if 'student_id' in session:
        user = Student.query.filter(Student.id == session['student_id']).first()
        return jsonify(success=True, student=user.to_dict())

    return jsonify(success=False), 401

## need to modify login based on states 
@mod_student.route('/login', methods=['POST'])
def login():
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError as e:
        return render_template('student_login.html',message = "This enter valid credentials")

    user = Student.query.filter(Student.email == email).first()
    if user is None or not user.check_password(password):
        return render_template('student_login.html' , message = "Invalid credentials")

    session['student_id'] = user.id

    return jsonify(success=True, student=user.to_dict())


@mod_student.route('/registerpage',methods=['GET'])
def registerpage():
    return render_template('student_regester.html')


@mod_student.route('/logout', methods=['POST'])
def logout():
    session.pop('student_id')
    return jsonify(success=True)


@mod_student.route('/register', methods=['POST'])
def create_student():
    try:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        cgpa  = request.form['cgpa']
        rollno = request.form['rollno']
    except KeyError as e:
        return render_template('student_regester.html',message="please fill all the fields")


    if '@' not in email:
        return render_template('student_regester.html' , message = "please enter valid email address")
    if  float(cgpa) <= 0 or float(cgpa) >= 10:
        return render_template('student_regester.html' , message="please enter valid cgpa")  
    if int(rollno) >= 20169999 or int(rollno) <= 20120000:
        return render_template('student_regester.html' , message="please enter valid roll number")     
    u = Student(name, email, cgpa , rollno , password)
    db.session.add(u)


    try:
        db.session.commit()
    except IntegrityError as e:
        return jsonify('regester.html', message="This email or roll number already exists")
    return jsonify(success = True)



@mod_student.route('/getall' , methods=['GET'])
def getall():
    students = Student.query.all()
    users = []
    for student in students:
        users.append(student.to_dict())
    return jsonify(students= users)
