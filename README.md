# Project Description

This project is about automatically generating questions on non-verbal reasoning. This is to help generate multiple question sets (and solutions) of comparable difficulty to help students practice questions on non-verbal reasoning (inspired by RS Agarwal's question types). It is based on a series of parameter controlled rules - for the difficulty level, question types, etc. For instance, the question on paper folding, rotation, etc., will decide how 'complicated' the pattern is based on difficulty level. Likewise, the type of polygon (how many sides?) is also determined through a parameter. Distractors for multiple choice questions are generated through the same code (small transformations on the original solution.) 

At the school level, it develops 3D and geometrical reasoning for kids and at the college level is useful for placement test preparation, etc., and otherwise as well, just a good exercise for the brain with ready scoring (since the answer sets are automatically generated with the question)!  

# Links
Conference - http://t4e2019.unigoa.ac.in/
Github     - https://github.com/GiriB/turtle

# Setup Instruction

- Setup Python2 virtual environment
- Install packages from requirements.txt
- Create following folder structure

```
./plot/
├── quads
├── seq
├── series
└── trans
```



# CutImage.py

Question Full Image - plot(i).png
Distractor FUll Image - plot(i)Dist(j).png


- Solution Quadrant - plotQuad(i).png
- Actual Question - Solution Remaining 3 parts - plotRest(i).png

- Distractors Quadrant (same number as solution) - plotQuad(i)Dist(j).png
Distractors Remaining 3 parts - plotQuad(i)Dist(j).png

- Combination of all 4 answer options - output(i).png

















# TODO

1. package this in a manner that can be easily used by someone to generate multiple sets of papers with as many questions as necessary of comparable difficulty level
2. "Field testing"
3. analytics pending for the paper


- NLP - question generation, ask similar phrases, not same always. hard code for now
- cognitive neuro science - stanford - alzheimer's, dementia kept away
- CAT exam, NATA exam - data interpretation

- testing:
- turing test
- RS agarwal - non vr questions
- ask if the question is machine generated
- automated question generation using discourse markers, NLP - date -> when?, place -> where?. quantifying? -> coherence, plausibility
- scoring, time taken, feedback
  - interesting, 

- different difficulty levels, different quizzes
- or multiple types in same paper. make google form and collect feedback

assessment:
- automated generation - compare machine generated vs manual generation (turing test)
- does the question and answer make sense? 
  - did the person understand the question? 
  - is the question clear?
  - is fold really fold? is dice really dice?
  - is the solution correct? or is it random?
- is the question difficult? do the parameters really control the difficulty? time taken by the person? did they get the answer right?
- what is the impact of people solving these questions? over time, is there improvement in their understanding?


- generate the solution and store the solution too

host on amazon turk? for larger user responses?

website:
- leaderboard - hide/publish score?
- login - to track improvement over time and multiple attempts?
- quiz up
- gamification aspect

geometric reasoning and interpretation



timeline planning


# Questions

1. Draft of the paper is ready? - no
2. What is the main novel contribution of this work?
3. Which theme/track will we apply for in the T4E conference? - theme 1
4. Why the focus on non-verbal reasoning?
   - needed by many MOOCs and exams
   - difficult to create manually
   - high cost of creating good quality questions
   - manually constructed questions have poor performance parameters
5. authors order? first, second etc.
6. is the conference decided, or can we explore some more?
7. need to check if all the functional requirements mentioned in the report have been completed.
8. how to test for difficulty level of a question? 



# Timeline

- complete coding by July 1st
- complete paper writing by July 10th 



# Team

Akshay Shrivastava
Giri Bhatnagar
Gowri Srinivasa
Hardik Mahipal Surana