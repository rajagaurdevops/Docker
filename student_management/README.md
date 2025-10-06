# Student Management System

A simple web-based **Student Management System** built with **Python**, **Flask**, and **SQLite**.  
This project allows you to **add, edit, delete, and view students**, with a database to store their details.

---

## Features

- Add new students with **Name, Roll Number, Branch, and Contact**.
- Edit existing student information.
- Delete students.
- View all students in a table.
- Data is stored in a local SQLite database (`students.db`).

---

## Technologies Used

- Python 3.x
- Flask
- SQLite
- HTML/CSS (templates in `templates/` folder)
- Flask's `render_template` for dynamic pages

---

## Project Structure

student_management/<br>
├── `app.py`   # Main Flask application<br>
├── `students.db`   # SQLite database (auto-created)<br>
├── `requirements.txt`   # Python dependencies<br>
├── `templates/`   # HTML templates (index.html, add.html, edit.html)<br>
├── `static/`  # Static files (CSS, JS)<br>
├── `venv/`  # Python virtual environment



---

## Setup Instructions

1. **Clone the repository**:

```bash
git clone <repository-url>
cd student_management
```


# Create virtual environment (if not created yet)
```
python3 -m venv venv
```

# Activate it (macOS/Linux)
```
source venv/bin/activate
```

# Activate it (Windows)
```
venv\Scripts\activate
```

# Install dependencies:
```
pip install -r requirements.txt
```
```
python3 app.py
```

## Using the Application

1. **Open the Application**  
   Open your browser and go to:  
   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

2. **Home Page**  
   - Displays a table of all students with their details:
     - ID
     - Name
     - Roll Number
     - Branch
     - Contact
     - Actions (Edit / Delete)

3. **Add a New Student**  
   - Click **Add New Student**.  
   - Fill in the form fields:  


# SQLite Database Guide
The app uses SQLite database (students.db) located in the project folder.
Access Database<br>
You can open the database in terminal:

```
sqlite3 students.db
```

usefull command<br>
.tables                -- List all tables<br>
.schema students       -- Show table structure<br>
SELECT * FROM students; -- View all student records<br>
.exit                  -- Exit SQLite




