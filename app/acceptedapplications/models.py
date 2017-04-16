from flask_sqlalchemy import SQLAlchemy
from app import db
from flask import *
from app.student.models import *
from app.faculty.models import *

class AcceptedApplication(db.Model):
    __tablename__= 'acceptedapplication'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)	
    student_id=db.Column(db.Integer,db.ForeignKey('student.id'))
    faculty_id=db.Column(db.Integer,db.ForeignKey('faculty.id'))

    def __init__(self,student_id,faculty_id):
        self.student_id=student_id
        self.faculty_id=faculty_id
    

    
