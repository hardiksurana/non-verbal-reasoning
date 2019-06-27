from flask import Flask, render_template, redirect, url_for, request
import requests
from random import shuffle
import json
import sys, os
sys.path.insert(0, os.path.dirname(os.getcwd()))

from generateQuestionPaper import generate_questions

# create the application object
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/Users/hardik/Desktop/projects/turtle/webapp/static/result/'

NUM_SETS = 1
NUM_QUESTIONS = 3   # number of questions in quiz
NUM_POLYGONS = 2    # indicative of difficulty level
NUM_OPTIONS = 3     # number of answer options
questions = dict()
responses = dict()
current_question = 1
student_details = None

def calculate(questions, responses):
    pass

@app.route('/', methods = ['GET'])
def home():
    return render_template('home.html')

@app.route('/submitDetails', methods = ['POST'])
def submitDetails():
    global current_question
    global questions
    if request.method == 'POST':
        student_details = request.form
        # render the quiz page with the first question
        questions = generate_questions(NUM_QUESTIONS, NUM_POLYGONS, NUM_OPTIONS).copy()
        distractors = questions[str(current_question)]['distractors']
        answer = questions[str(current_question)]['answer']
        distractors.append(str(answer))
        shuffle(distractors)

        # print json.dumps(questions, sort_keys=True, indent=4)
        return render_template("quiz.html", 
        question_text = questions[str(current_question)]['question_text'],
        question_filepath = questions[str(current_question)]['question'],
        options = distractors
        # options = shuffle(questions[str(current_question)]['distractors'].append(questions[str(current_question)]['answer']))
        )

@app.route('/generate', methods = ['GET', 'POST'])
def generate():
    global current_question
    global questions
    global responses
    if request.method == 'POST':
        responses[str(current_question)] = dict()
        responses[str(current_question)]["response"] = request.form['options']
        responses[str(current_question)]["time_in_seconds"] = request.form['timeTaken']
        print "\nQuestion = {0}. Response = {1}. Answer = {2}\n".format(str(current_question), responses[str(current_question)], questions[str(current_question)]['answer'])
        current_question += 1
        if current_question <= NUM_QUESTIONS:
            distractors = questions[str(current_question)]['distractors']
            answer = questions[str(current_question)]['answer']
            distractors.append(str(answer))
            shuffle(distractors)
            
            return render_template("quiz.html", 
            question_text = questions[str(current_question)]['question_text'],
            question_filepath = questions[str(current_question)]['question'],
            options = distractors
            )
        else:
            print json.dumps(responses, sort_keys=True, indent=4)
            current_question = 1
            questions = dict()
            responses = dict()
            print("quiz is completed")
            return render_template("home.html")
            # result = calculate(questions, responses)

if __name__ == "__main__":
    app.run(debug=True,port=9000)