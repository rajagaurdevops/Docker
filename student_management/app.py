from flask import Flask, render_template, request, redirect, url_for, flash, abort
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Regexp, Optional
import os

# Initialize Flask application
app = Flask(__name__)

# Secret key for session management, CSRF protection in forms
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Replace with a random key in production

# SQLite database configuration
# The database file will be created in the same directory as this script
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(os.path.abspath(__file__)), 'students.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable tracking modifications for performance

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# -------------------------
# Database model for Student
# -------------------------
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Auto-incrementing primary key
    name = db.Column(db.String(100), nullable=False)  # Student name
    roll_no = db.Column(db.String(20), unique=True, nullable=False)  # Unique roll number
    branch = db.Column(db.String(50), nullable=False)  # Branch/department
    contact = db.Column(db.String(20), nullable=True)  # Optional contact number

    def __repr__(self):
        return f'<Student {self.name} - {self.roll_no}>'

# -------------------------
# Flask-WTF form for adding/editing students
# -------------------------
class StudentForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(message='Name is required'),
        Length(min=2, max=100, message='Name must be between 2 and 100 characters')
    ])
    roll_no = StringField('Roll No', validators=[
        DataRequired(message='Roll No is required'),
        Length(min=1, max=20, message='Roll No must be between 1 and 20 characters'),
        Regexp(r'^[A-Za-z0-9-]+$', message='Roll No can only contain letters, numbers, and hyphens')
    ])
    branch = StringField('Branch', validators=[
        DataRequired(message='Branch is required'),
        Length(min=2, max=50, message='Branch must be between 2 and 50 characters')
    ])
    contact = StringField('Contact', validators=[
        Optional(),
        Length(min=10, max=20, message='Contact must be between 10 and 20 characters if provided'),
        Regexp(r'^\+?[1-9]\d{1,14}$', message='Contact must be a valid phone number')
    ])
    submit = SubmitField('Submit')  # Submit button

# -------------------------
# Create database tables if they don't exist
# -------------------------
with app.app_context():
    db.create_all()

# -------------------------
# Home route: Display all students
# -------------------------
@app.route('/')
def index():
    students = Student.query.all()  # Fetch all students from database
    return render_template('index.html', students=students)

# -------------------------
# Add new student route
# -------------------------
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    form = StudentForm()
    if form.validate_on_submit():  # Check if form is valid on POST
        # Check if roll_no already exists
        existing = Student.query.filter_by(roll_no=form.roll_no.data).first()
        if existing:
            flash('Roll No already exists. Please use a unique Roll No.', 'error')
            return render_template('add.html', form=form)
        
        # Create new student object
        student = Student(
            name=form.name.data,
            roll_no=form.roll_no.data,
            branch=form.branch.data,
            contact=form.contact.data or None
        )
        db.session.add(student)  # Add to session
        db.session.commit()      # Save to database
        flash('Student added successfully!', 'success')
        return redirect(url_for('index'))  # Redirect to home page
    return render_template('add.html', form=form)

# -------------------------
# Edit student route
# -------------------------
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get_or_404(id)  # Fetch student by ID or return 404
    form = StudentForm(obj=student)  # Pre-fill form with existing data
    
    if form.validate_on_submit():
        # Check if new roll_no conflicts with another student
        existing = Student.query.filter(
            Student.roll_no == form.roll_no.data,
            Student.id != id
        ).first()
        if existing:
            flash('Roll No already exists for another student. Please use a unique Roll No.', 'error')
            return render_template('edit.html', form=form, student=student)
        
        # Update student details
        student.name = form.name.data
        student.roll_no = form.roll_no.data
        student.branch = form.branch.data
        student.contact = form.contact.data or None
        db.session.commit()
        flash('Student updated successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('edit.html', form=form, student=student)

# -------------------------
# Delete student route
# -------------------------
@app.route('/delete/<int:id>')
def delete_student(id):
    student = Student.query.get_or_404(id)  # Fetch student by ID or 404
    db.session.delete(student)  # Delete from session
    db.session.commit()         # Commit changes
    flash('Student deleted successfully!', 'success')
    return redirect(url_for('index'))

# -------------------------
# Error handler for 404
# -------------------------
@app.errorhandler(404)
def not_found(error):
    flash('Page not found.', 'error')
    return redirect(url_for('index'))

# -------------------------
# Run the Flask app
# -------------------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure database tables are created
    app.run(debug=True, port=8000, host='0.0.0.0')  # Accessible from any network
