from flask import Flask, render_template, redirect, url_for, request, session
import requests
from random import shuffle
import json
import uuid
import sys, os
sys.path.insert(0, os.path.dirname(os.getcwd()))

from generateQuestionPaper import generate_questions

# create the application object
app = Flask(__name__)
app.secret_key = "non_verbal_reasoning"
app.config['UPLOAD_FOLDER'] = '/Users/hardik/Desktop/projects/turtle/webapp/static/result/'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

NUM_SETS = 1
NUM_QUESTIONS = 3   # number of questions in quiz
NUM_POLYGONS = 2    # indicative of difficulty level
NUM_OPTIONS = 3     # number of answer options
questions = dict()
responses = dict()
feedback_dict = dict()

# current_question = 1
student_details = None

def calculate(questions, responses):
    pass

@app.route('/', methods = ['GET'])
def home():
    if 'user_id' in session:
        session.pop('user_id', None)
    if 'user_name' in session:
        session.pop('user_name', None)
    if 'current_question' in session:
        session.pop('current_question', None)
    return render_template('home.html')

@app.route('/enterQuiz', methods = ['POST'])
def enterQuiz():
    global questions

    if request.method == 'POST':
        # collect user's details
        student_details = request.form
        session['user_id'] = uuid.uuid1().hex
        print("session user_id = " + session['user_id'])
        session['user_name'] = student_details['user_name']
        session['current_question'] = 1

        # generate the quiz questions
        questions = generate_questions(session['user_id'], NUM_QUESTIONS, NUM_POLYGONS, NUM_OPTIONS).copy()
        
        # render the quiz page with the first question
        distractors = questions[str(session['current_question'])]['distractors']
        answer = questions[str(session['current_question'])]['answer']
        distractors.append(str(answer))
        shuffle(distractors)

        # print json.dumps(questions, sort_keys=True, indent=4)
        return render_template("quiz.html", 
        question_text = questions[str(session['current_question'])]['question_text'],
        question_filepath = questions[str(session['current_question'])]['question'],
        options = distractors
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