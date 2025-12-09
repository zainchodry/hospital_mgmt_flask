# Hospital Management System

This is a web-based Hospital Management System built using Flask. It allows administrators to manage doctors, patients, and appointments efficiently. The system also provides role-based access for doctors and patients.

## Features

- **Admin Role**:
  - Manage doctors and patients.
  - View and book appointments.
- **Doctor Role**:
  - View their appointments.
- **Patient Role**:
  - Book appointments with doctors.
  - View their appointment history.

## Technologies Used

- **Backend**: Flask, Flask-SQLAlchemy, Flask-Migrate, Flask-Login, Flask-WTF
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd hospital_mgmt_flask
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:

   ```bash
   flask db upgrade
   ```

5. Run the application:

   ```bash
   python run.py
   ```

6. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Project Structure

- `app/`: Contains the application code.
  - `routes/`: Contains route definitions for authentication and main functionalities.
  - `models.py`: Defines the database models.
  - `forms.py`: Contains form definitions using Flask-WTF.
  - `extenshions.py`: Initializes Flask extensions.
- `templates/`: Contains HTML templates for the frontend.
- `config.py`: Configuration file for the application.
- `run.py`: Entry point to run the application.
- `requirements.txt`: Lists the Python dependencies.

## Usage

1. **Register**: Create an account as a patient or doctor.
2. **Login**: Access the dashboard based on your role.
3. **Admin Dashboard**:
   - Add and manage doctors and patients.
   - Book and view appointments.
4. **Doctor Dashboard**:
   - View appointments with patients.
5. **Patient Dashboard**:
   - Book appointments with doctors.
   - View appointment history.

## License

This project is licensed under the MIT License. Feel free to use and modify it as per your needs.

---

For any issues or contributions, please create a pull request or open an issue in the repository.
