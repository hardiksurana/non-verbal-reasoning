from flask import Flask, render_template, redirect, url_for, request, session
from mysql_utils import MySQL
import requests
from random import shuffle
import json
import uuid
import base64
import sys, os
sys.path.insert(0, os.path.dirname(os.getcwd()))

from generateQuestionPaper import generate_questions, generate_question

# create the application object
app = Flask(__name__)
app.secret_key = "non_verbal_reasoning"
app.config['UPLOAD_FOLDER'] = '/Users/hardik/Desktop/projects/turtle/webapp/static/result/'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

NUM_QUESTIONS = 2   # number of questions in quiz
NUM_POLYGONS = 2    # indicative of difficulty level
NUM_OPTIONS = 3     # number of answer options
questions = dict()
responses = dict()
feedback_dict = dict()

# current_question = 1
student_details = None

db = MySQL()

def calculate(questions, responses):
    pass

@app.route('/', methods = ['GET'])
def home():
    # clear any existing session
    if 'user_id' in session:
        session.pop('user_id', None)
    if 'session_id' in session:
        session.pop('session_id', None)
    if 'current_question' in session:
        session.pop('current_question', None)
    if 'question_id' in session:
        session.pop('question_id', None)
    if 'response_id' in session:
        session.pop('response_id', None)
    return render_template('login.html')

@app.route('/login', methods = ['POST'])
def login():
    email = request.form['email']
    db.curr.execute("SELECT * FROM users WHERE email='{0}';".format(email))
    
    # email exists - generate quiz
    if db.curr.rowcount == 1:
        print("user found in db")
        user_details = db.curr.fetchall()[0]
        session['user_id'] = user_details['user_id']
        session['session_id'] = uuid.uuid1().hex
        db.curr.execute("INSERT INTO sessions (session_id, user_id) VALUES ('{0}', '{1}');".format(session['session_id'], session['user_id']))
        db.conn.commit()
        print("session stored in db")
        return render_template('main.html', login_msg="You are logged in as " + user_details['email'])
    
    # email does not exist - redirect to register
    else:
        print("user not found in db")
        return render_template('register.html')

@app.route('/register', methods = ['POST'])
def register():
    email = request.form['email']
    age = request.form['age']
    education = request.form['education']
    gender = request.form['gender']

    db.curr.execute("INSERT INTO users (email, age, education, gender) VALUES ('{0}', {1}, '{2}', '{3}');".format(email, age, education, gender))
    db.conn.commit()
    print("user added to db")

    db.curr.execute("SELECT * FROM users WHERE email='{0}';".format(email))
    user_details = db.curr.fetchall()[0]
    session['user_id'] = user_details['user_id']
    session['session_id'] = uuid.uuid1().hex
    db.curr.execute("INSERT INTO sessions (session_id, user_id) VALUES ('{0}', '{1}');".format(session['session_id'], session['user_id']))
    db.conn.commit()
    print("session stored in db")
    return render_template('main.html', login_msg="You are registered as " + user_details['email'])


@app.route('/enterQuiz', methods = ['POST'])
def enterQuiz():
    print("user id = " + str(session['user_id']))
    print("session id = " + str(session['session_id']))
    if 'current_question' not in session:
        session['current_question'] = 1

    # generate the quiz questions
    question_id = generate_question(session['current_question'], session['user_id'], session['session_id'])['question_id']
    session['question_id'] = question_id
    print("question generated. question_id = " + str(question_id))

    db.curr.execute("SELECT TO_BASE64(question_img) as ques_img, TO_BASE64(answer_img) as ans_img, TO_BASE64(distractor_1_img) as dist_1_img, TO_BASE64(distractor_2_img) as dist_2_img, TO_BASE64(distractor_3_img) as dist_3_img FROM questions WHERE question_id={0};".format(question_id))
    if db.curr.rowcount > 0:
        result = db.curr.fetchall()[0]
        return render_template("quiz.html", 
            question_text = "identify the missing piece of the image",
            question = result['ques_img'],
            answer = result['ans_img'],
            dist_1 = result['dist_1_img'],
            dist_2 = result['dist_2_img'],
            dist_3 = result['dist_3_img']
        )

@app.route('/feedback', methods = ['POST'])
def feedback():
    # store response image of the user
    response_base64_string = request.form["options"]
    time_taken = request.form["timeTaken"]
    insert_query = """INSERT INTO responses (user_id, session_id, question_id, response_img, time_taken_in_secs) VALUES (%s, %s, %s, FROM_BASE64(%s), %s)"""
    db.curr.execute(insert_query, (session['user_id'], session['session_id'], session['question_id'], response_base64_string, time_taken))
    db.conn.commit()
    print("response image and time taken stored in responses table")

    select_query = """SELECT response_id from responses WHERE user_id=%s AND session_id=%s AND question_id=%s"""
    db.curr.execute(select_query, (session['user_id'], session['session_id'], session['question_id']))
    if db.curr.rowcount == 1:
        result = db.curr.fetchall()[0]
        session['response_id'] = result['response_id']
        print("response id = " + str(session['response_id']))
    else:
        print("failed to retrieve response from db")

    return render_template("feedback.html")

@app.route('/generate', methods = ['POST'])
def generate():
    machine_generated = request.form['machineGenerated']
    difficulty_scale = request.form["difficultyScale"]
    interesting_question = request.form["interestingQuestion"]
    clear_question = request.form['clearQuestion']
    challenging_question = request.form['challengingQuestion']
    induced_thinking = request.form['inducedThinking']

    # update response row in db with feedback data
    update_query = """UPDATE responses SET machine_generated=%s, difficulty_scale=%s, interesting_question=%s, clear_question=%s, challenging_question=%s, induced_thinking=%s WHERE response_id=%s"""
    db.curr.execute(update_query, (machine_generated, difficulty_scale, interesting_question, clear_question, challenging_question, induced_thinking, session['response_id']))
    db.conn.commit()
    print("feedback data updated to responses table")
    
    session['current_question'] += 1
    if session['current_question'] <= NUM_QUESTIONS:
        # generate the quiz questions
        question_id = generate_question(session['current_question'], session['user_id'], session['session_id'])['question_id']
        session['question_id'] = question_id
        print("question generated. question_id = " + str(question_id))

        db.curr.execute("SELECT TO_BASE64(question_img) as ques_img, TO_BASE64(answer_img) as ans_img, TO_BASE64(distractor_1_img) as dist_1_img, TO_BASE64(distractor_2_img) as dist_2_img, TO_BASE64(distractor_3_img) as dist_3_img FROM questions WHERE question_id={0};".format(question_id))
        if db.curr.rowcount > 0:
            result = db.curr.fetchall()
            return render_template("quiz.html", 
                question_text = "identify the missing piece of the image",
                question = result[0]['ques_img'],
                answer = result[0]['ans_img'],
                dist_1 = result[0]['dist_1_img'],
                dist_2 = result[0]['dist_2_img'],
                dist_3 = result[0]['dist_3_img']
            )
    else:
        # clear the session
        session.pop('user_id', None)
        session.pop('session_id', None)
        session.pop('question_id', None)
        session.pop('response_id', None)
        session.pop('current_question', None)
        print("quiz is completed")
        return render_template('main.html', login_msg="You have completed the quiz!")
        # result = calculate(questions, responses)


if __name__ == "__main__":
    # app.run(debug=True, port=9000)
    app.run(host="0.0.0.0", debug=True, port=5000)
    # app.run()