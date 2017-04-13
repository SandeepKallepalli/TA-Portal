from flask_sqlalchemy import SQLAlchemy
from app import db
from app import student,faculty
from student import models
from faculty import models

class AcceptedApplication(db.model):
    __tablename__= 'acceptedapplication'
    id=db.column(db.Integer,primary_key=True,autoincrement=True)	
    student_id=db.column(db.Integer,db.ForeignKey('student.id'))
    faculty_id=db.column(db.Integer,db.ForeignKey('faculty.id'))

    def __init__(self,student_id,faculty_id):
        self.student_id=student_id
        self.faculty_id=faculty_id
    

    
