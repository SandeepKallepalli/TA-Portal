from flask import *
from sqlalchemy.exc import IntegrityError
from app import db
from .models import Student

mod_acceptedapplication = Blueprint('acceptedapplication', __name__, url_prefix='/acceptedapplication')



