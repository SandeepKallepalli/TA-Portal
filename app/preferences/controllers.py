from flask import *
from sqlalchemy.exc import IntegrityError
from app import db

mod_preferences = Blueprint('preferences', __name__, url_prefix='/preferences')


