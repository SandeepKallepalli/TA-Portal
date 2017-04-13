from flask import *
from sqlalchemy.exc import IntegrityError
from app import db
from app import student

mod_application = Blueprint('application', __name__, url_prefix='/application')

#@mod_application.route('/<student>/getall',methods=['GET'])
#def studApplAll():

