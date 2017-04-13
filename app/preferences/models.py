from flask_sqlalchemy import SQLAlchemy
from flask import *
from app import db
from app.student.models import *
from app.faculty.models import *

class Preference(db.Model):
    __tablename__= 'preference'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)	
    student_id=db.Column(db.Integer,db.ForeignKey('student.id'))
    faculty1_id=db.Column(db.Integer,db.ForeignKey('faculty.id'))
    faculty2_id=db.Column(db.Integer,db.ForeignKey('faculty.id'))
    faculty3_id=db.Column(db.Integer,db.ForeignKey('faculty.id'))

    def __init__(self,student_id,faculty1_id,faculty2_id,faculty3_id):
        self.student_id=student_id
        self.faculty1_id=faculty1_id
        self.faculty2_id=faculty2_id
        self.faculty3_id=faculty3_id

    
