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

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Default environmental variables
# ENV SERVER_PORT 80
# ENV ENABLE_SSH true

# install requirements
RUN pip2 install -r requirements.txt

# Configure ports
# EXPOSE 2222 80
EXPOSE 8000

# setup ssh connection to container
# ENV SSH_PASSWD "root:Docker!"

# Run apt-get, to install the SSH server, and supervisor
# RUN apt-get update \
#     && apt-get install -y supervisor \
#     && apt-get install -y --no-install-recommends dialog \
#     && apt-get update \
#     && apt-get install -y --no-install-recommends openssh-server \
#     && echo "$SSH_PASSWD" | chpasswd  \
#     && rm -rf /var/lib/apt/lists/* \
#     && apt-get clean

# Copy the sshd_config file to its new location
# COPY sshd_config /etc/ssh/

# Start the SSH service
# RUN service ssh start

# start scripts
# COPY runapp.sh start.sh /usr/bin/

# supervisor config
# ADD supervisor/app.conf /etc/supervisor/conf.d/

# Run the chmod command to change permissions on above file in the /bin directory
# RUN chmod 755 /usr/bin/runapp.sh && chmod 755 /usr/bin/start.sh

# Entrypoint
# CMD "/usr/bin/start.sh"



CMD ["gunicorn", "--config", "./src/gunicorn_conf.py", "application:app"]
