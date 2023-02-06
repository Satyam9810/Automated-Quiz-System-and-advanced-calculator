# Advanced Quiz System and Mathematical Calculator

## Overview
This project is a web application that provides two main functionalities:
1. **Automated Quiz System**: Allows users to register, login, take quizzes, and view their scores.
2. **Mathematical Calculator**: A calculator that can handle complex mathematical expressions.

## Features
- User registration and login
- Multiple quizzes with various categories
- Timer for each quiz
- Score calculation and storage
- Result analytics
- Handles addition, subtraction, multiplication, division, modulus, and brackets
- Supports complex mathematical expressions
- Provides step-by-step solutions

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/AdvancedQuizCalculator.git
    cd AdvancedQuizCalculator
    ```

2. **Set up a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies**:
    ```bash
    pip install flask
    ```

4. **Initialize the database**:
    ```bash
    sqlite3 db/database.db < init_db.sql
    ```

5. **Run the application**:
    ```bash
    python app.py
    ```

## Usage
- Visit `http://127.0.0.1:5000` in your web browser.
- Register a new account or log in with existing credentials.
- Take quizzes and use the calculator.

## File Structure
- `app.py`: Main application file
- `calculator.py`: Handles mathematical calculations
- `quiz.py`: Handles quiz operations
- `user.py`: Handles user operations
- `db/`: Contains the SQLite database
- `static/`: Contains static files (CSS, JavaScript)
- `templates/`: Contains HTML templates

## Contributing
Feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License.
