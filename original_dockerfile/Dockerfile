# set base image (host OS)
FROM python:3.8

#remove bin/sh (shell) and add a symlink (soft) from shell to bash (if a command uses the shell it will be redirected to bash)
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

#update sources.list file with updated versions of repositories 
RUN apt-get -y update

#install curl, nano, wget, nginx, and git
RUN apt-get install -y curl nano wget nginx git

#get the gpg key for yarn package manager (the key is used to validate installs and downloads)
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -

#add respository to yarn.list sources.list.d directory (on running apt update, the main sources.list file will be updated with yarn.list)
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list


# Mongo
# sym link between echo and systemctl
RUN ln -s /bin/echo /bin/systemctl

#install gnupg and curl
RUN apt-get install gnupg curl

#get gpg key for mongodb, similar to yarn
RUN curl -fsSL https://pgp.mongodb.com/server-7.0.asc | gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor

#add repository to sources.list (similar to yarn above)
RUN echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-7.0.list
#RUN wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc |  apt-key add -
#RUN wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add -
#RUN echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-6.0.list
RUN apt-get -y update

#install mongodb
RUN apt install -y mongodb-org

# Install Yarn
RUN apt-get install -y yarn

#skip easy_install since it's deprecated and pip is included in newer python images
# Install PIP
#RUN easy_install pip

#add environment variables
ENV ENV_TYPE staging
ENV MONGO_HOST mongo
ENV MONGO_PORT 27017
ENV DATABASE adb
ENV TODO_COLLECTION todos
##########
ENV PYTHONPATH=$PYTHONPATH:/src/

# copy the dependencies file to the working directory
COPY src/requirements.txt .

# install dependencies
RUN pip install -r requirements.txt
