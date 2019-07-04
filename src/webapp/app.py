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
    if 'user_id' in session:
        session.pop('user_id', None)
    if 'session_id' in session:
        session.pop('session_id', None)
    if 'current_question' in session:
        session.pop('current_question', None)
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
    return render_template('main.html', login_msg="You are registered as " + user_details['email'])


@app.route('/enterQuiz', methods = ['POST'])
def enterQuiz():
    if 'current_question' not in session:
        session['current_question'] = 1

    # generate the quiz questions
    # questions = generate_questions(session['user_id'], NUM_QUESTIONS, NUM_POLYGONS, NUM_OPTIONS).copy()
    
    question_id = generate_question(session['current_question'], session['user_id'], session['session_id'])['question_id']
    print("question_id = " + str(question_id))

    # select_query = "SELECT * FROM questions WHERE question_id=5;"
    db.curr.execute("SELECT TO_BASE64(question_img) as ques_img, TO_BASE64(answer_img) as ans_img, TO_BASE64(distractor_1_img) as dist_1_img, TO_BASE64(distractor_2_img) as dist_2_img, TO_BASE64(distractor_3_img) as dist_3_img FROM questions WHERE question_id={0};".format(question_id))
    if db.curr.rowcount > 0:
        result = db.curr.fetchall()
        # print(result[0]['ques_img'])
        # render the quiz page with the first question
        # distractors = questions[str(session['current_question'])]['distractors']
        # answer = questions[str(session['current_question'])]['answer']
        # distractors.append(str(answer))
        # shuffle(distractors)
        # return render_template('main.html', login_msg="image is created successfully and stored in db")

        # print json.dumps(questions, sort_keys=True, indent=4)
        return render_template("quiz.html", 
        question_text = "identify the missing piece of the image",
        question = result[0]['ques_img'],
        answer = result[0]['ans_img'],
        dist_1 = result[0]['dist_1_img'],
        dist_2 = result[0]['dist_2_img'],
        dist_3 = result[0]['dist_3_img']
        )

@app.route('/feedback', methods = ['POST'])
def feedback():
    global questions
    global feedback_dict
    global responses

    if request.method == 'POST':
        # store responses of the user
        responses[str(session['current_question'])] = dict()
        responses[str(session['current_question'])]["response"] = request.form["options"]
        responses[str(session['current_question'])]["time_in_seconds"] = request.form["timeTaken"]
        print "\nQuestion = {0}. Response = {1}. Answer = {2}\n".format(str(session['current_question']), responses[str(session['current_question'])], questions[str(session['current_question'])]['answer'])
        # session['current_question'] += 1

        # render the feedback page            
        if session['current_question'] <= NUM_QUESTIONS:
            return render_template("feedback.html")
        else:
            print json.dumps(responses, sort_keys=True, indent=4)
            session.pop('user_id', None)
            session.pop('user_name', None)
            session.pop('current_question', None)
            questions = dict()
            responses = dict()
            feedback_dict = dict()

            print("quiz is completed")
            return render_template("home.html")
            # result = calculate(questions, responses)

@app.route('/generate', methods = ['POST'])
def generate():
    global questions
    global feedback_dict
    global responses

    if request.method == 'POST':
        feedback_dict[str(session['current_question'])] = dict()
        feedback_dict[str(session['current_question'])]["machineGenerated"] = request.form["machineGenerated"]
        feedback_dict[str(session['current_question'])]["difficultyScale"] = request.form["difficultyScale"]
        feedback_dict[str(session['current_question'])]["interestingQuestion"] = request.form["interestingQuestion"]
        feedback_dict[str(session['current_question'])]["questionClear"] = request.form["questionClear"]
        
        
        session['current_question'] += 1
        if session['current_question'] <= NUM_QUESTIONS:
            distractors = questions[str(session['current_question'])]['distractors']
            answer = questions[str(session['current_question'])]['answer']
            distractors.append(str(answer))
            shuffle(distractors)
            
            return render_template("quiz.html", 
            question_text = questions[str(session['current_question'])]['question_text'],
            question_filepath = questions[str(session['current_question'])]['question'],
            options = distractors
            )
        else:
            print json.dumps(responses, sort_keys=True, indent=4)
            print json.dumps(feedback_dict, sort_keys=True, indent=4)
            session.pop('user_id', None)
            session.pop('user_name', None)
            session.pop('current_question', None)
            questions = dict()
            responses = dict()
            feedback_dict = dict()
            print("quiz is completed")
            return render_template("home.html")
            # result = calculate(questions, responses)


if __name__ == "__main__":
    # app.run(debug=True, port=9000)
    app.run(host="0.0.0.0", debug=True, port=5000)
    # app.run()