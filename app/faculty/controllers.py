from flask import Blueprint,request,session,jsonify
from sqlalchemy.exc import IntegrityError
from app import db
from .models import Faculty

mod_faculty=Blueprint('faculty',__name__,url_prefix='/faculty')

@mod_faculty.route('/login',methods=['GET'])
def check_login():
    if '
