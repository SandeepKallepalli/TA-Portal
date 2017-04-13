from flask import *
from sqlalchemy.exc import IntegrityError
from app import db

mod_application = Blueprint('application', __name__, url_prefix='/application')

#@mod_application.route('/<student>/getall',methods=['GET'])
#def studApplAll():

