from flask import *
from sqlalchemy.exc import IntegrityError
from app import db
from .models import *
mod_preferences = Blueprint('preferences', __name__, url_prefix='/preferences')


