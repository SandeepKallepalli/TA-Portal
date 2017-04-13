from flask import *
from sqlalchemy.exc import IntegrityError
from app import db
from .models import *

mod_finalta = Blueprint('finalta', __name__, url_prefix='/finalta')


