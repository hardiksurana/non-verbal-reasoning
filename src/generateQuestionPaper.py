'''
# tunable parameters
- number of questions
- number of answer options
- question types
- type of polygon
- difficulty level
'''

'''
# format to store quiz data in dictionary
{
    set_<SET_NUM>: {
        <Question_Number> : {
            'question_type': 'cut' / 'fold' / 'dice' ...,
            'question': <Path_To_Question_Image>,
            'answer': <Path_To_Solution_Image>,
            'distractors': [<Path_To-Dist_1>,<Path_To-Dist_2>,<Path_To-Dist_3>]
        }
    }
}
'''

'''
# Data to be collected for analytics
question type, difficulty level, right/wrong selection, time taken, question clear?, difficulty experienced? 
'''

import argparse
from cutImage import Cut
import json
from webapp.mysql_utils import MySQL

# def generate_questions(sets, questionNum, polyNum, optionNum):
#     questions = dict()

#     for s in range(1, sets + 1):
#         questions["set_" + str(s)] = dict()
#         if questionNum is not None:
#             for i in range(1, questionNum + 1):
#                 c = Cut(polyNum, i, s, optionNum)
#                 questions["set_" + str(s)]['q' + str(i)] = dict()
#                 questions["set_" + str(s)]['q' + str(i)]['question_type'] = 'cut'
#                 c.genQuestionAnswerPair()
#                 c.genDistractors()
#                 questions["set_" + str(s)]['q' + str(i)]['question'] = c.getQuestion()
#                 questions["set_" + str(s)]['q' + str(i)]['answer'] = c.getAnswer()
#                 questions["set_" + str(s)]['q' + str(i)]['distractors'] = c.getDistractors()
#     # print json.dumps(questions, sort_keys=True, indent=4)
#     return questions


'''
# format to store quiz data in dictionary
{
    '<Question_Number>' : {
        'question_type': 'cut' / 'fold' / 'dice' ...,
        'question_text': 'identify the missing piece of the image'
        'question': <Path_To_Question_Image>,
        'answer': <Path_To_Solution_Image>,
        'distractors': ['<Path_To-Dist_1>','<Path_To-Dist_2>','<Path_To-Dist_3>']
    }
}
'''
def generate_questions(user_id, questionNum, polyNum, optionNum):
    questions = dict()
    if questionNum is not None:
        for i in range(1, questionNum + 1):
            c = Cut(user_id, polyNum, i, 1, optionNum)
            questions[str(i)] = dict()
            questions[str(i)]['question_type'] = 'cut'
            questions[str(i)]['num_polygons'] = polyNum
            questions[str(i)]['question_text'] = 'identify the missing piece of the image'
            c.genQuestionAnswerPair()
            c.genDistractors()
            questions[str(i)]['question'] = c.getQuestion()
            questions[str(i)]['answer'] = c.getAnswer()
            questions[str(i)]['distractors'] = c.getDistractors()
    # print json.dumps(questions, sort_keys=True, indent=4)
    return questions


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
    
    # cut
    if question_num in [1, 2]:
        c = Cut(user_id, session_id, polygon_num, question_num)
        c.generate_question_answer_pair()
        question_filepath = c.getQuestion()
        answer_filepath = c.getAnswer()
        c.genDistractors()
        distractors_filepaths = c.getDistractors()

        with open(question_filepath, 'rb') as f:
            question_binary = f.read()

        with open(answer_filepath, 'rb') as f:
            answer_binary = f.read()

        distractors_binary = []
        for distractors_filepath in distractors_filepaths:
            with open(distractors_filepath, 'rb') as f:
                dist_binary = f.read()
                distractors_binary.append(dist_binary)

        insert_query = """INSERT INTO questions (user_id, session_id, question_type, question_img, answer_img, distractor_1_img, distractor_2_img, distractor_3_img, num_polygons) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        db.curr.execute(insert_query, (user_id, session_id, "cut", question_binary, answer_binary, distractors_binary[0], distractors_binary[1], distractors_binary[2], polygon_num))
        db.conn.commit()
        print("question saved in db")

    # dice
    elif question_num in [3, 4]:
        pass
    # fold
    elif question_num in [5, 6]:
        pass
    # sequence
    elif question_num in [7, 8]:
        pass
    # grid
    elif question_num in [9, 10]:
        pass
    # series
    elif question_num in [11, 12]:
        pass
    # transform
    elif question_num in [13, 14]:
        pass
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
    


if __name__ == "__main__":
    # parse input arguments
    parser= argparse.ArgumentParser(description='Enter paramters to tune to generate question paper')
    parser.add_argument('--cut', type=int, help='enter number of \'cut\' questions to be generated')
    # parser.add_argument('--dice', type=int, help='enter number of \'dice\' questions to be generated')
    # parser.add_argument('--figure', type=int, help='enter number of \'figure\' questions to be generated')
    # parser.add_argument("--fold", type=int, help="enter number of \'fold\' questions to be generated")
    # parser.add_argument("--sequence", type=int, help="enter number of \'sequence\' questions to be generated")
    # parser.add_argument('--series', type=int, help='enter number of \'series\' questions to be generated')
    parser.add_argument('--polyNum', required=True, type=int, help='enter number of polygons embedded in outer polygon')
    parser.add_argument('--optionNum', type=int, help='enter number of options to be generated along with the answer')
    # parser.add_argument('--sets', type=int, help='enter number of question paper sets to be generated')

    args= parser.parse_args()
    # questions = generate_questions(args.sets, args.cut, args.polyNum, args.optionNum)
    questions = generate_questions(args.cut, args.polyNum, args.optionNum)
