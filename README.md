# Project Description

Non-verbal reasoning tests allow evaluators to test a diverse set of abilities in students without relying upon, or being limited by, language skills. In this paper we present an automated system to generate a variety of non-verbal reasoning questions spanning abstract reasoning, non-verbal analogy and spatial reasoning question types with granular control over difficulty levels. Our design also generates meaningful distractors as this is an important aspect of generating better quality multiple-choice questions. We present experimental results through analytics on question feedback and performance that demonstrate that the system-generated questions indeed serve to assess and hone non- verbal reasoning skills.

The website is currently hosted [here](https://nvr-quiz.azurewebsites.net)

# Setup Instruction

It is preferable to run the application within docker to ensure all dependencies are met.

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
pip2 install -r requirements.txt

# enter into hosted/local mysql instance
mysql -h <HOST_NAME> -P <PORT_NUMBER> -u <USER_NAME> -p

# create a database using the dump file in the mysql shell
mysql> source <PATH_TO_DB_DUMP>

# start gunicorn web server in another terminal
venv/bin/gunicorn application:app -b 0:8000 --access-logfile '-' --worker-class gevent
# or, use pre-set configurations
venv/bin/gunicorn --config ./app/src/gunicorn_conf.py application:app

# Run the docker container locally to test
docker build --tag nvrquiz_docker_image .
# access the web application on http://0.0.0.0/
docker run -p 80:8000 nvrquiz_docker_image
```

# Deployment Instructions

1. Create a 'Web App for Containers' in Microsoft Azure - [link](https://docs.microsoft.com/en-us/azure/app-service/containers/tutorial-custom-docker-image)
  - Deploy to Docker Hub instead of Azure Container Registry
1. Create a MySQL database in AWS - [link](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Tutorials.WebServerDB.CreateDBInstance.html)

# Team

1. Giri Bhatnagar
2. Akshay Shrivastava
3. Hardik Mahipal Surana

# Guide

Dr. Gowri Srinivasa