from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('kars-landing-page.html')

# Add routes for other pages
@app.route('/academicschedule')
def academic_schedule():
    return render_template('academic_schedule.html')

@app.route('/fests')
def fests():
    return render_template('fest.html')

@app.route('/login')
def login():
    return render_template('login.html')