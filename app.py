from flask import Flask, render_template, redirect, url_for, request, session, flash
from quiz import Quiz
from user import User
from calculator import calculate

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.login(username, password):
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.register(username, password):
            flash('Registration successful')
            return redirect(url_for('login'))
        else:
            flash('User already exists')
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    quizzes = Quiz.get_all_quizzes()
    return render_template('dashboard.html', quizzes=quizzes)

@app.route('/quiz/<quiz_id>', methods=['GET', 'POST'])
def take_quiz(quiz_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        answers = request.form.to_dict()
        score = Quiz.submit_quiz(quiz_id, session['username'], answers)
        flash(f'You scored {score}')
        return redirect(url_for('dashboard'))
    quiz = Quiz.get_quiz(quiz_id)
    return render_template('quiz.html', quiz=quiz)

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    result = None
    expression = None
    if request.method == 'POST':
        expression = request.form['expression']
        result = calculate(expression)
    return render_template('calculator.html', result=result, expression=expression)

if __name__ == '__main__':
    app.run(debug=True)
