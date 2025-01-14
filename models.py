from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from db import db

db = SQLAlchemy()

# Database model
class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    upload_time = db.Column(db.String(50), nullable=False)
    resume_data = db.Column(db.LargeBinary, nullable=True)  # Column to store PDF as binary data
    resume_filename = db.Column(db.String(100), nullable=True)  # Optional: Store the file name

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Watch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    visit_count = db.Column(db.Integer, default=0)
