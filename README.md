# Project Description

This project is about automatically generating questions on non-verbal reasoning. This is to help generate multiple question sets (and solutions) of comparable difficulty to help students practice questions on non-verbal reasoning (inspired by RS Agarwal's question types). It is based on a series of parameter controlled rules - for the difficulty level, question types, etc. For instance, the question on paper folding, rotation, etc., will decide how 'complicated' the pattern is based on difficulty level. Likewise, the type of polygon (how many sides?) is also determined through a parameter. Distractors for multiple choice questions are generated through the same code (small transformations on the original solution.) 

At the school level, it develops 3D and geometrical reasoning for kids and at the college level is useful for placement test preparation, etc., and otherwise as well, just a good exercise for the brain with ready scoring (since the answer sets are automatically generated with the question)!  

1. Why the focus on non-verbal reasoning?
   - needed by many MOOCs and exams
   - difficult to create manually
   - high cost of creating good quality questions
   - manually constructed questions have poor performance parameters


# Setup Instruction

- Setup Python2 virtual environment
- Install packages from requirements.txt
- Create following folder structure
```bash
git clone https://github.com/hardiksurana/non-verbal-reasoning.git
```

# TODO
1. "Field testing"
2. analytics
3. assessment:
  - compare machine generated vs manual generation (turing test)
  - is the solution correct? or is it random?
  - is the question difficult? do the parameters really control the difficulty? time taken by the person? did they get the answer right?
  - what is the impact of people solving these questions? over time, is there improvement in their understanding?


# Team
Akshay Shrivastava
Giri Bhatnagar
Hardik Mahipal Surana

# Guide
Dr. Gowri Srinivasa