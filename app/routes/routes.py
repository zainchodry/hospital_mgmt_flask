from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.models import *
from app.forms import *
from app.extenshions import *
from flask_login import login_user, logout_user, current_user, login_required

main = Blueprint("main", __name__)

@main.route('/')
def index():
    doctors = Doctor.query.limit(6).all()
    return render_template('index.html', doctors=doctors)

@main.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'admin':
        doctors = Doctor.query.all()
        patients = Patient.query.all()
        appointments = Appointment.query.order_by(Appointment.date.desc()).all()
        return render_template('dashboard.html', doctors=doctors, patients=patients, appointments=appointments)
    elif current_user.role == 'doctor':
        my_doctor = Doctor.query.filter_by(email=current_user.email).first()
        appointments = my_doctor.appointments if my_doctor else []
        return render_template('dashboard.html', appointments=appointments, doctors=None, patients=None)
    else:
        patient = Patient.query.filter_by(email=current_user.email).first()
        appointments = patient.appointments if patient else []
        return render_template('dashboard.html', appointments=appointments, doctors=None, patients=None)
    

@main.route('/doctors', methods=['GET','POST'])
@login_required
def doctors():
    if current_user.role != 'admin':
        flash('Only admins can access doctors list.')
        return redirect(url_for('main.dashboard'))
    form = DoctorForm()
    if form.validate_on_submit():
        d = Doctor(name=form.name.data, speciality=form.speciality.data, phone=form.phone.data, email=form.email.data)
        db.session.add(d)
        db.session.commit()
        flash('Doctor added.')
        return redirect(url_for('main.doctors'))
    doctors = Doctor.query.all()
    return render_template('doctors.html', doctors=doctors, form=form)


@main.route('/patients', methods=['GET','POST'])
@login_required
def patients():
    if current_user.role != 'admin':
        flash('Only admins can access patients list.')
        return redirect(url_for('main.dashboard'))
    form = PatientForm()
    if form.validate_on_submit():
        p = Patient(name=form.name.data, age=form.age.data, phone=form.phone.data, email=form.email.data)
        db.session.add(p)
        db.session.commit()
        flash('Patient added.')
        return redirect(url_for('main.patients'))
    patients = Patient.query.all()
    return render_template('patients.html', patients=patients, form=form)


@main.route('/appointments', methods=['GET','POST'])
@login_required
def appointments():
    form = AppointmentForm()
    form.patient_id.choices = [(p.id, p.name) for p in Patient.query.all()]
    form.doctor_id.choices = [(d.id, d.name) for d in Doctor.query.all()]
    if form.validate_on_submit():
        appt = Appointment(patient_id=form.patient_id.data, doctor_id=form.doctor_id.data, date=form.date.data, reason=form.reason.data)
        db.session.add(appt)
        db.session.commit()
        flash('Appointment booked.')
        return redirect(url_for('main.appointments'))
    appts = Appointment.query.order_by(Appointment.date.desc()).all()
    return render_template('appointments.html', appointments=appts, form=form)