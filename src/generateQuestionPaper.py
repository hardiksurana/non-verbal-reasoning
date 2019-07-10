'''
# tunable parameters
- number of questions
- number of answer options
- question types
- type of polygon
- difficulty level
'''

import argparse
from cutImage import Cut
from dice import Dice
from series import Series
from figureMatrixAndSequence import FigureMatrixAndSequence
import json
from webapp.mysql_utils import MySQL

def generate_question(question_num, user_id, session_id):
    '''
    by default:
    even questions are easy, odd questions are difficult
    2 questions - 1 easy, 1 difficult per question type
    '''
    db = MySQL()
    # set the difficulty level
    if question_num % 2 == 0:
        polygon_num = 4
    else:
        polygon_num = 2
    
    # # cut
    # if question_num in [1, 2]:
    #     c = Cut(user_id, session_id, polygon_num, question_num)
    #     c.generate_question_answer_pair()
    #     question_filepath = c.getQuestion()
    #     answer_filepath = c.getAnswer()
    #     c.genDistractors()
    #     distractors_filepaths = c.getDistractors()

    #     with open(question_filepath, 'rb') as f:
    #         question_binary = f.read()

    #     with open(answer_filepath, 'rb') as f:
    #         answer_binary = f.read()

    #     distractors_binary = []
    #     for distractors_filepath in distractors_filepaths:
    #         with open(distractors_filepath, 'rb') as f:
    #             dist_binary = f.read()
    #             distractors_binary.append(dist_binary)

    #     insert_query = """INSERT INTO questions (user_id, session_id, question_type, question_img, answer_img, distractor_1_img, distractor_2_img, distractor_3_img, num_polygons) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    #     db.curr.execute(insert_query, (user_id, session_id, "cut", question_binary, answer_binary, distractors_binary[0], distractors_binary[1], distractors_binary[2], polygon_num))
    #     db.conn.commit()
    #     print("cut question saved in db")

    # # dice
    # elif question_num in [3, 4]:
        # d = Dice(user_id, session_id, question_num)
        # d.generate_question()
        # question_filepath = d.getQuestion()
        # d.generate_answer()
        # answer_filepath = d.getAnswer()
        # d.generate_distractors()
        # distractors_filepaths = d.getDistractors()

        # with open(question_filepath, 'rb') as f:
        #     question_binary = f.read()

        # with open(answer_filepath, 'rb') as f:
        #     answer_binary = f.read()

        # distractors_binary = []
        # for distractors_filepath in distractors_filepaths:
        #     with open(distractors_filepath, 'rb') as f:
        #         dist_binary = f.read()
        #         distractors_binary.append(dist_binary)

        # insert_query = """INSERT INTO questions (user_id, session_id, question_type, question_img, answer_img, distractor_1_img, distractor_2_img, distractor_3_img, num_polygons) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        # db.curr.execute(insert_query, (user_id, session_id, "dice", question_binary, answer_binary, distractors_binary[0], distractors_binary[1], distractors_binary[2], 0))
        # db.conn.commit()
        # print("dice question saved in db")

    # fold
    # elif question_num in [5, 6]:
    if question_num in [1,2]:
        pass

    # figure matrix and sequence
    # elif question_num in [7, 8]:
    #     f = FigureMatrixAndSequence(user_id, session_id, question_num)
    #     f.generate_all_images()
    #     question_filepath = f.get_question()
    #     print("question_filepath = " + question_filepath)
    #     answer_filepath = f.get_answer()
    #     print("answer_filepath = " + answer_filepath)
    #     distractors_filepaths = f.get_distractors()
    #     print(str(distractors_filepaths))

    #     with open(question_filepath, 'rb') as f:
    #         question_binary = f.read()

    #     with open(answer_filepath, 'rb') as f:
    #         answer_binary = f.read()

    #     distractors_binary = []
    #     for distractors_filepath in distractors_filepaths:
    #         with open(distractors_filepath, 'rb') as f:
    #             dist_binary = f.read()
    #             distractors_binary.append(dist_binary)

    #     insert_query = """INSERT INTO questions (user_id, session_id, question_type, question_img, answer_img, distractor_1_img, distractor_2_img, distractor_3_img, num_polygons) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    #     db.curr.execute(insert_query, (user_id, session_id, "figMatrix", question_binary, answer_binary, distractors_binary[0], distractors_binary[1], distractors_binary[2], 0))
    #     db.conn.commit()
    #     print("figure matrix & sequence question saved in db")

    # # grid
    # elif question_num in [9, 10]:
    #     pass

    # series
    # elif question_num in [11, 12]:
    #     pass
    #     s = Series(user_id, session_id, question_num)
    #     s.generate_all_images()
    #     question_filepath = s.get_question()
    #     answer_filepath = s.get_answer()
    #     distractors_filepaths = s.get_distractors()

    #     with open(question_filepath, 'rb') as f:
    #         question_binary = f.read()

    #     with open(answer_filepath, 'rb') as f:
    #         answer_binary = f.read()

    #     distractors_binary = []
    #     for distractors_filepath in distractors_filepaths:
    #         with open(distractors_filepath, 'rb') as f:
    #             dist_binary = f.read()
    #             distractors_binary.append(dist_binary)

    #     insert_query = """INSERT INTO questions (user_id, session_id, question_type, question_img, answer_img, distractor_1_img, distractor_2_img, distractor_3_img, num_polygons) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    #     db.curr.execute(insert_query, (user_id, session_id, "series", question_binary, answer_binary, distractors_binary[0], distractors_binary[1], distractors_binary[2], 0))
    #     db.conn.commit()
    #     print("series question saved in db")

    else:
        pass
    
    select_query = """SELECT question_id from questions WHERE user_id=%s AND session_id=%s"""
    db.curr.execute(select_query, (user_id, session_id))
    if db.curr.rowcount > 0:
        print("question id in genrateQuestion = ")
        result = db.curr.fetchall()[-1]
        return result
    else:
        print("failed to retrieve question from db")
        return -1