# EduTrack - Student Management System

A comprehensive Django-based student management system for educational institutions.

## Features

- **User Authentication**: Secure login/logout system
- **Student Management**: Complete CRUD operations for student records
- **Academic Tracking**: Track student enrollment status and academic levels
- **Photo Upload**: Upload and manage student profile photos
- **Admin Interface**: Django admin integration for easy management
- **Responsive Design**: Bootstrap-based responsive UI
- **Age Calculation**: Automatic age calculation from birth date
- **Search & Pagination**: Advanced search and pagination for large datasets

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd EduTrack
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv env
   ```

3. **Activate virtual environment:**
   - Windows: `env\Scripts\activate`
   - Linux/Mac: `source env/bin/activate`

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure database:**
   - Update database settings in `AcademiX/settings.py`
   - Run migrations:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

6. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```

7. **(Optional) Populate sample data:**
   ```bash
   python manage.py populate_sample_data --count=50
   ```

8. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

9. **Access the application:**
   - Login page: http://127.0.0.1:8000/accounts/login/
   - Main application: http://127.0.0.1:8000/ (after login)
   - Admin interface: http://127.0.0.1:8000/admin/

## Project Structure

```
EduTrack/
├── AcademiX/                 # Main Django project
│   ├── settings.py          # Project settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
├── apps/
│   ├── core/               # Core app for dashboard
│   │   ├── templates/      # Base templates
│   │   └── static/         # Static files (CSS, JS, images)
│   └── student_management/ # Student management app
│       ├── models.py       # Student model
│       ├── views.py        # CRUD views
│       ├── forms.py        # Django forms
│       ├── urls.py         # App URLs
│       ├── admin.py        # Admin configuration
│       └── templates/      # App templates
├── media/                  # Uploaded media files
├── env/                    # Virtual environment
├── manage.py               # Django management script
└── requirements.txt        # Python dependencies
```

## Features Overview

### Student Management
- Add new students with personal and academic information
- View detailed student profiles
- Edit student information
- Delete students with confirmation
- Upload student photos

### Academic Levels
- Primary 1-6
- Secondary 1-6

### Enrollment Status
- Active
- Transferred
- Dismissed
- Graduated

## Authentication

The application uses Django's built-in authentication system:

- **Login**: Access the application at `/accounts/login/`
- **Logout**: Click on the user profile dropdown in the header and select "Sign Out"
- **Protected Views**: All application views require user authentication
- **Admin Access**: Superusers can access the Django admin at `/admin/`

## Technologies Used

- **Backend**: Django 6.0.3
- **Database**: MySQL
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **JavaScript**: jQuery, Bootstrap JS
- **Authentication**: Django Auth System
- **Icons**: Bootstrap Icons, Boxicons

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.