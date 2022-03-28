from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


nkosl_app = Flask(__name__)
nkosl_app.config.from_object(Config)
db = SQLAlchemy(nkosl_app)
migrate = Migrate(nkosl_app, db)

from app import routes
