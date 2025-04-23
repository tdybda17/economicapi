###########
# BUILDER #
###########

# pull official base image
FROM python:3.12.8-bullseye AS builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get -y update

RUN export PKG_CONFIG_PATH="${PKG_CONFIG_PATH}:/usr/local/opt/libffi/lib/pkgconfig"
# install dependencies
RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

#########
# FINAL #
#########

FROM python:3.12.8-bullseye

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN adduser app && usermod -a -G app app

RUN apt-get -y update

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/economicapi
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

# install dependencies
# RUN apk update && apk add libpq busybox-suid
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x $APP_HOME/entrypoint.sh

# copy project
COPY . $APP_HOME
RUN rm -rf $APP_HOME/tests
RUN rm -rf $APP_HOME/.git
RUN rm -rf $APP_HOME/.github
RUN rm -rf $APP_HOME/.idea
RUN rm -rf $APP_HOME/venv
RUN rm -rf $APP_HOME/.venv

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

# run entrypoint.sh
ENTRYPOINT ["/home/app/economicapi/entrypoint.sh"]
