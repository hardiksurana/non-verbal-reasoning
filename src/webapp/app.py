from flask import Flask, render_template, redirect, url_for, request, session
# from mysql_utils import MySQL
from src.webapp.mysql_utils import MySQL
import requests
from random import shuffle
import json
import uuid
import base64
import sys, os
# sys.path.insert(0, os.path.dirname(os.getcwd()))
# from generateQuestionPaper import generate_question
from src.generateQuestionPaper import generate_question

# create the application object
app = Flask(__name__)
app.secret_key = "non_verbal_reasoning"
app.config['UPLOAD_FOLDER'] = '/Users/hardik/Desktop/projects/turtle/webapp/static/result/'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["THREADS_PER_PAGE"] = 2


# total number of questions in quiz
NUM_QUESTIONS = 12

db = MySQL()

def calculate_score_report():
    # finds the number of correct answers for current user in current session
    select_correct_answers_query = """SELECT COUNT(*) AS score FROM responses JOIN questions WHERE responses.question_id=questions.question_id AND responses.user_id=%s AND responses.session_id=%s AND TO_BASE64(questions.answer_img)=TO_BASE64(responses.response_img)"""
    db.curr.execute(select_correct_answers_query, (session['user_id'], session['session_id']))
    if db.curr.rowcount > 0:
        score = db.curr.fetchall()[0]['score']

        # find total number of questions by current user in current session
        select_count_questions_query = """SELECT COUNT(*) AS num_questions FROM questions WHERE questions.user_id=%s AND questions.session_id=%s"""
        db.curr.execute(select_count_questions_query, (session['user_id'], session['session_id']))
        if db.curr.rowcount > 0:
            num_questions = db.curr.fetchall()[0]['num_questions']
            return (score, num_questions)

def calculate_leaderboard():
    leaderboard_select_query = """SELECT score, num_questions, num_attempts, TIME_TAKEN, email, ROUND(score*100/num_questions, 0) AS percentage FROM 
    (
        SELECT COUNT(*) AS score, responses.user_id AS RES_UID 
        FROM responses JOIN questions 
        WHERE responses.question_id=questions.question_id AND TO_BASE64(questions.answer_img)=TO_BASE64(responses.response_img) 
        GROUP BY RES_UID
    ) ans 
    JOIN 
    (
        SELECT COUNT(question_id) AS num_questions, COUNT(DISTINCT(session_id)) as num_attempts, user_id as QUE_UID 
        FROM questions 
        GROUP BY QUE_UID
    ) que on ans.RES_UID=que.QUE_UID 
    JOIN 
    (
        SELECT avg(time_taken_in_secs) as TIME_TAKEN, user_id as TIME_UID 
        from responses 
        group by user_id
    ) time on que.QUE_UID=time.TIME_UID 
    JOIN 
    (
        SELECT email, user_id AS USER_UID 
        from users
    ) USER ON time.TIME_UID=USER.USER_UID
    ORDER BY percentage DESC"""
    
    db.curr.execute(leaderboard_select_query)
    if db.curr.rowcount > 0:
        return db.curr.fetchall()
    else:
        return []

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

    print("previous session cleared")
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

@app.route('/logout', methods=['GET'])
def logout():
    return redirect('/', code=302)

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
            question_text = "Identify the piece that completes the figure.",
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
    # cut
    if session['current_question'] in [1, 2]:
        question_text = "Identify the image that completes the figure."
    # dice
    elif session['current_question'] in [3, 4]:
        question_text = "Identify the cube box that is made out of the given image."
    # fold
    elif session['current_question'] in [5, 6]:
        question_text = "Identify the image which shows how the pattern would appear when the given image is folded on the dotted line."
    # figure matrix and sequence
    elif session['current_question'] in [7, 8]:
        question_text = "Identify the image which will continue the same series as the given 5 images."
    # grid
    elif session['current_question'] in [9, 10]:
        question_text = "Identify the image follows the same pattern as the images in each row."
    # series
    elif session['current_question'] in [11, 12]:
        question_text = "Identify the next image in the series."

    if session['current_question'] <= NUM_QUESTIONS:
        # generate the quiz questions
        question_id = generate_question(session['current_question'], session['user_id'], session['session_id'])['question_id']
        session['question_id'] = question_id
        print("question generated. question_id = " + str(question_id))

        db.curr.execute("SELECT TO_BASE64(question_img) as ques_img, TO_BASE64(answer_img) as ans_img, TO_BASE64(distractor_1_img) as dist_1_img, TO_BASE64(distractor_2_img) as dist_2_img, TO_BASE64(distractor_3_img) as dist_3_img FROM questions WHERE question_id={0};".format(question_id))
        if db.curr.rowcount > 0:
            result = db.curr.fetchall()
            return render_template("quiz.html", 
                question_text = question_text,
                question = result[0]['ques_img'],
                answer = result[0]['ans_img'],
                dist_1 = result[0]['dist_1_img'],
                dist_2 = result[0]['dist_2_img'],
                dist_3 = result[0]['dist_3_img']
            )
    else:
        # quiz has ended, calculate score
        score, num_questions = calculate_score_report()
        print("quiz is completed")
        if isinstance(score, int) and isinstance(num_questions, int) and num_questions > 0:
            return render_template('main.html', login_msg="You have completed the quiz! Your score is {0}%".format(str(float((score*100)/num_questions))))


@app.route('/leaderboard', methods = ['GET'])
def leaderboard():
    result = calculate_leaderboard()
    return render_template("leaderboard.html", leaderboard=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)