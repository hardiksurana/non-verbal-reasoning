# Project Description

This project is about automatically generating questions on non-verbal reasoning. This is to help generate multiple question sets (and solutions) of comparable difficulty to help students practice questions on non-verbal reasoning (inspired by RS Agarwal's question types). It is based on a series of parameter controlled rules - for the difficulty level, question types, etc. For instance, the question on paper folding, rotation, etc., will decide how 'complicated' the pattern is based on difficulty level. Likewise, the type of polygon (how many sides?) is also determined through a parameter. Distractors for multiple choice questions are generated through the same code (small transformations on the original solution.) 

At the school level, it develops 3D and geometrical reasoning for kids and at the college level is useful for placement test preparation, etc., and otherwise as well, just a good exercise for the brain with ready scoring (since the answer sets are automatically generated with the question)!  

1. Why the focus on non-verbal reasoning?
   - needed by many MOOCs and exams
   - difficult to create manually
   - high cost of creating good quality questions
   - manually constructed questions have poor performance parameters


# Setup Instruction

```sh
# clone the repository
git clone https://github.com/hardiksurana/non-verbal-reasoning.git

# enter project root directory
cd non-verbal-reasoning

# setup virtual environment
pip2 install virtualenv
virtualenv -p python2.7 venv

# activate virtual environment
source venv/bin/activate

# install dependencies
apt-get install libpng freetype
apt-get install libfreetype6, pkg-config, libfreetype6-dev, libpng-dev
pip2 install six
pip2 install -r requirements.txt

/usr/local/mysql-8.0.16-macos10.14-x86_64/bin/mysql -h <HOST> -P <PORT> -u <USERNAME> -p
mysql> source /Users/hardik/Desktop/projects/turtle/scripts/db_dump.sql

# start gunicorn web server in another terminal
venv/bin/gunicorn --bind=0.0.0.0 --timeout 600 application:app
```


# Links

- https://medium.com/@nikovrdoljak/deploy-your-flask-app-on-azure-in-3-easy-steps-b2fe388a589e
- https://nvr-quiz.azurewebsites.net


# TODO

1. "Field testing"
2. analytics
3. assessment:
  - compare machine generated vs manual generation (turing test)
  - is the solution correct? or is it random?
  - is the question difficult? do the parameters really control the difficulty? time taken by the person? did they get the answer right?
  - what is the impact of people solving these questions? over time, is there improvement in their understanding?


# Team

1. Giri Bhatnagar
2. Akshay Shrivastava
3. Hardik Mahipal Surana

# Guide

Dr. Gowri Srinivasa