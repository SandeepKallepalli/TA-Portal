from flask_sqlalchemy import SQLAlchemy
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Faculty(db.model):
    __tablename__="faculty"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.column(db.string(255))
    email=db.column(db.string(255),unique=True)
    course_id=db.column(db.string(6),unique=True)
    course_name=db.column(db.string(255))
    course_description=db.column(db.string(1000))
    passwd=db.column(db.string(255))

    def __init__(self,name,email,course_id,course_name,course_description,passwd):
        self.name=name
        self.email=email
        self.course_id=course_id
        self.course_name=course_name
        self.course_description=course_description
        self.passwd=passwd
    def check_password(self, password):
        return check_password_hash(self.password, password)
    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'email':self.email,
            'course_id':self.course_id
            'course_name':self.course_name
            'course_description':self.course_description
            'passwd':self.passwd
        }
        def __repr__(self):
            return "Faculty<%d> %s" %(self.id,self.name)
        

