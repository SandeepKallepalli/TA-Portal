from flask import *
from sqlalchemy.exc import IntegrityError
from app import db
from .models import *
mod_nomination = Blueprint('nomination', __name__, url_prefix='/nomination')




