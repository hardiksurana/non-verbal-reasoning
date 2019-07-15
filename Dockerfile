FROM python:2.7

# matplotlib
RUN apt-get update \
    && apt-get install -y libfreetype6 pkg-config libfreetype6-dev libpng-dev

# opencv
RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get install -y cmake libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev \
    && apt-get install -y libglib2.0-0 libsm6 libxext6 libxrender-dev \
    && apt-get install -y libatlas-base-dev gfortran \
    && apt-get install -y python-opencv

RUN echo "installed all pre-requisites for matplotlib and opencv"

RUN mkdir /app

# working directory
WORKDIR /app

# copy current directory into the container
ADD . /app

# install requirements
RUN pip2 install -r requirements.txt

# setup ssh connection to container
ENV SSH_PASSWD "root:Docker!"
RUN apt-get update \
    && apt-get install -y --no-install-recommends dialog \
    && apt-get update \
    && apt-get install -y --no-install-recommends openssh-server \
    && echo "$SSH_PASSWD" | chpasswd 
# COPY sshd_config /etc/ssh/
EXPOSE 8000 2222
# RUN service ssh start

CMD ["gunicorn", "--config", "./src/gunicorn_conf.py", "application:app"]