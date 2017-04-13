from flask import *
from sqlalchemy.exc import IntegrityError
from app import db

mod_finalta = Blueprint('finalta', __name__, url_prefix='/finalta')


