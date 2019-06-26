from flask import Flask, render_template, redirect, url_for, request
import requests
import json
import sys, os
sys.path.insert(0, os.path.dirname(os.getcwd()))

from src.generateQuestionPaper import generate_questions

# create the application object
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/Users/hardik/Desktop/projects/turtle/webapp/static/result/'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate', methods = ['POST'])
def generate():
    if request.method == 'POST':
        result = request.form
        questions = generate_questions(1, 3, 2, 3)
        print json.dumps(questions, sort_keys=True, indent=4)


        return render_template("quiz.html", questions = questions)



if __name__ == "__main__":
    app.run(debug=True,port=9000)