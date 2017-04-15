from flask_sqlalchemy import SQLAlchemy
from flask import *
from app.student.models import *
from app.faculty.models import *
from app import db

class Nomination(db.Model):
    __tablename__= 'nomination'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)	
    student_id=db.Column(db.Integer,db.ForeignKey('student.id'))
    faculty_id=db.Column(db.Integer,db.ForeignKey('faculty.id'))

    def __init__(self,student_id,faculty_id):
        self.student_id=student_id
        self.faculty_id=faculty_id


    
