import sqlite3

class Quiz:
    @staticmethod
    def get_all_quizzes():
        conn = sqlite3.connect('db/database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM quizzes')
        quizzes = cursor.fetchall()
        conn.close()
        return quizzes

    @staticmethod
    def get_quiz(quiz_id):
        conn = sqlite3.connect('db/database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM quizzes WHERE id = ?', (quiz_id,))
        quiz = cursor.fetchone()
        cursor.execute('SELECT * FROM questions WHERE quiz_id = ?', (quiz_id,))
        questions = cursor.fetchall()
        conn.close()
        return {'quiz': quiz, 'questions': questions}

    @staticmethod
    def submit_quiz(quiz_id, username, answers):
        conn = sqlite3.connect('db/database.db')
        cursor = conn.cursor()
        score = 0
        for qid, ans in answers.items():
            cursor.execute('SELECT correct_answer FROM questions WHERE id = ?', (qid,))
            correct_answer = cursor.fetchone()[0]
            if ans == correct_answer:
                score += 1
        cursor.execute('INSERT INTO results (quiz_id, username, score) VALUES (?, ?, ?)', (quiz_id, username, score))
        conn.commit()
        conn.close()
        return score
