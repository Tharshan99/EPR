from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint, send_file, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from flask_login import current_user, LoginManager, UserMixin, login_required, logout_user, login_user
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from io import BytesIO

# hashed_password = generate_password_hash(password, method='pbkdf2:sha256')


from flask_security import (
    auth_required,
    current_user,
)

pages = Blueprint('pages', __name__)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)  # Attach LoginManager to the app
login_manager.login_view = 'login'  # Replace 'login' with the name of your login route

# Define a user loader callback for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Example: SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications for performance

db = SQLAlchemy(app)

# Update these configurations
GMAIL_USER = 'rajahtharshan99@gmail.com'
GMAIL_PASSWORD = 'aotn efbk qlst ebfn'

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

# Create database tables
with app.app_context():
    # db.drop_all()
    # print("All tables dropped.")
    db.create_all()


# @app.route('/', methods=['GET'])
# def index():
#     if current_user.is_authenticated:
#         return redirect(url_for('pages.dashboard'))
#     return redirect(url_for('security.login')) #general login

##################################################### Login

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Retrieve the user from the database
        user = User.query.filter_by(email=email).first()

        # Check if the user exists and the password is correct
        if not user or not check_password_hash(user.password, password):
            flash('Invalid email or password.', 'error')
            return redirect(url_for('login'))

        # Log in the user
        login_user(user)
        flash('Logged in successfully!', 'success')
        return redirect(url_for('dashboard'))  # Redirect to a protected page after login

    return render_template('pages/login.html')

##################################################### Home

@app.route('/home')
def career_page():
    # applications = Application.query.all()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('pages/career_page.html', current_time=current_time)

##################################################### Register

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists.', 'error')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('pages/register.html')

##################################################### Submit Application

@app.route('/submit-application', methods=['POST'])
def submit_application():
    name = request.form.get('name')
    email = request.form.get('email')
    category = request.form.get('category')
    resume = request.files.get('resume')
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if not resume:
        flash('Resume is required!', 'error')
        return redirect('/home')
    
    resume_data = resume.read()

    # Save the resume temporarily
    resume_path = os.path.join('uploads', resume.filename)
    os.makedirs('uploads', exist_ok=True)
    resume.save(resume_path)

    new_application = Application(name=name, email=email, category=category, upload_time=current_time, resume_data=resume_data, resume_filename=resume.filename)
    try:
        db.session.add(new_application)
        db.session.commit()
        # flash('Application stored in database successfully!', 'success')
    except Exception as e:
        flash(f'Error saving application to the database: {str(e)}', 'error')
        return redirect('/home')

    # Prepare email
    subject = f"New Application for {category}"
    body = f"Name: {name}\nEmail: {email}\nCategory: {category}"

    message = MIMEMultipart()
    message['From'] = GMAIL_USER
    message['To'] = 'tharshanthamizlan@gmail.com'
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    # Attach the resume
    with open(resume_path, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename={resume.filename}'
        )
        message.attach(part)

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            server.sendmail(GMAIL_USER, 'tharshanthamizlan@gmail.com', message.as_string())
        flash('Application submitted successfully!', 'success')
    except Exception as e:
        flash(f'Error sending application: {str(e)}', 'error')
    finally:
        # Clean up the uploaded file
        if os.path.exists(resume_path):
            os.remove(resume_path)

    return redirect('/home')

##################################################### Download Resume

@app.route('/download-resume/<int:application_id>')
def download_resume(application_id):
    application = Application.query.get(application_id)
    if not application or not application.resume_data:
        abort(404, description="Resume not found")
    
    return send_file(
        BytesIO(application.resume_data),  # Binary data stored in the database
        mimetype='application/pdf',
        as_attachment=True,
        download_name=application.resume_filename
    )

##################################################### Index

@app.route('/')
def index():
    return render_template('pages/index.html')


##################################################### Career Dashboard

@app.route('/career_dashboard')
@login_required
def career_dashboard():
    try:
        applications = Application.query.all()
        return render_template('pages/career_dashboard.html', applications=applications)
    except Exception as e:
        return f"An error occurred: {str(e)}", 500
    
@app.before_request
def before_request():
    if not current_user.is_authenticated and request.endpoint in ['dashboard']:
        flash('Please log in to access this page.', 'warning')

##################################################### Dashboard

@app.route('/dashboard')
@login_required
def dashboard():
    try:
        # applications = Application.query.all()
        return render_template('pages/dashboard.html')
    except Exception as e:
        return f"An error occurred: {str(e)}", 500
    
##################################################### Logout    

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
