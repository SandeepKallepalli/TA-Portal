from flask_sqlalchemy import SQLAlchemy
from app import db
from flask import *
from app.student.models import *
from app.faculty.models import *

class FinalTA(db.Model):
    __tablename__= 'finalta'
    id=db.column(db.Integer,primary_key=True,autoincrement=True)	
    student_id=db.column(db.Integer,db.ForeignKey('student.id'))
    faculty_id=db.column(db.Integer,db.ForeignKey('faculty.id'))

    def __init__(self,student_id,course_id):
        self.student_id=student_id
        self.faculty_id=faculty_id


    
