# pull official base image
FROM python:3.7-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./scripts/entrypoint.sh /usr/src/app/scripts/entrypoint.sh

# copy project
COPY . /usr/src/app/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/scripts/entrypoint.sh"]
#
## copy entrypoint.sh
#COPY scripts/entrypoint.sh /stockman_api/scripts/entrypoint.sh
##
#RUN ["chmod", "+x", "/stockman_api/scripts/entrypoint.sh"]
#
#ENTRYPOINT ["/stockman_api/scripts/entrypoint.sh"]
