from flask import *
from sqlalchemy.exc import IntegrityError
from app import db
from .models import *
from  app.faculty.models import *
from  app.student.models import *
from  app.application.models import *

mod_preferences = Blueprint('preferences', __name__ , url_prefix='/preferences')

@app.route('/preferences/addpreference',method=['POST'])
def create_preference():
    try:
        course1_id=request.form['course1_id']
        course2_id=request.form['course2_id']
        course3_id=request.form['course3_id']
    except KeyError as e:
        return render_template('student_home.html',message="please fill all the preferences")
    stud=Student.query.filter(Student.id==session['student_id']).first()
    preference1=Faculty.query.filter(Faculty.course_id==course1_id).first()
    preference2=Faculty.query.filter(Faculty.course_id==course2_id).first()
    preference3=Faculty.query.filter(Faculty.course_id==course3_id).first()
    pref=Preference(session['student_id'],preference1.id,preference2.id,preference3.id)
    app1=Application(session['student_id'],preferences1.id)
    app2=Application(session['student_id'],preferences2.id)
    app3=Application(session['student_id'],preferences3.id)
    try:
        db.session.add(pref)
        db.session.add(app1)
        db.session.add(app2)
        db.session.add(app3)
        db.session.commit()
    except IntegrityError as e:
        return render_template('student_home.html', message="Sorry Request Failed")
    return render_template('student_home2.html', student=stud , faculty1=preference1 , faculty2=preference2 , faculty3=preference3 )


