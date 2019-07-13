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
virtualenv -p venv

# activate virtual environment
source venv/bin/activate

# install dependencies
pip2 install -r requirements.txt

# start gunicorn web server
gunicorn -b 0.0.0.0:8080 wsgi:app --access-logfile '-' -w 4
```


# Setups
/usr/local/mysql-8.0.16-macos10.14-x86_64/bin/mysql -h nvrquiz-db-instance.chb3ppjrdtjp.ap-south-1.rds.amazonaws.com -P 3306 -u turtle -p
mysql> source /Users/hardik/Desktop/projects/turtle/scripts/db_dump.sql

https://medium.com/@nikovrdoljak/deploy-your-flask-app-on-azure-in-3-easy-steps-b2fe388a589e

## App Service enables you to access your app content through FTP/S:

FTPS endpoint: ftps://waws-prod-ma1-007.ftp.azurewebsites.windows.net/site/wwwroot
username: nvr-quiz\$nvr-quiz
password: AxctxKk5JuhR8wGMvBcXasbY6u7smzlcv4rcgE6Mo2FwYxQKhH8vzhd6NcM8

## URL
https://nvr-quiz.azurewebsites.net


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