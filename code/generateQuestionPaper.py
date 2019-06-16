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
    <Question_Number> : {
        'question_type': 'cut' / 'fold' / 'dice' ...,
        'question': <Path_To_Question_Image>,
        'answer': <Path_To_Solution_Image>,
        'distractors': [<Path_To-Dist_1>,<Path_To-Dist_2>,<Path_To-Dist_3>]
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

if __name__ == "__main__":
    # parse input arguments
    parser= argparse.ArgumentParser(description='Enter paramters to tune to generate question paper')
    parser.add_argument('--cut', type=int, help='enter number of \'cut\' questions to be generated')
    parser.add_argument('--dice', type=int, help='enter number of \'dice\' questions to be generated')
    parser.add_argument('--figure', type=int, help='enter number of \'figure\' questions to be generated')
    parser.add_argument("--fold", type=int, help="enter number of \'fold\' questions to be generated")
    parser.add_argument("--sequence", type=int, help="enter number of \'sequence\' questions to be generated")
    parser.add_argument('--series', type=int, help='enter number of \'series\' questions to be generated')
    # parser.add_argument('--sidesNum', required=True, type=int, help='enter number of sides in the polygon')
    parser.add_argument('--polyNum', required=True, type=int, help='enter number of polygons embedded in outer polygon')
    parser.add_argument('--optionNum', type=int, help='enter number of options to be generated along with the answer')
    args= parser.parse_args()

    questions = dict()

    if args.cut is not None:
        for i in range(1, args.cut + 1):
            c = Cut(args.polyNum, i, args.optionNum)
            questions[str(i)] = dict()
            questions[str(i)]['question_type'] = 'cut'

            c.genQuestionAnswerPair()
            c.genDistractors()

            questions[str(i)]['question'] = c.getQuestion()
            questions[str(i)]['answer'] = c.getAnswer()
            questions[str(i)]['distractors'] = c.getDistractors()

        
    print json.dumps(questions, sort_keys=True, indent=4)

