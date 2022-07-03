FROM ubuntu:20.04
WORKDIR /project
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0
ADD . /project
EXPOSE 5000
RUN apt-get update \
        && apt install -y python3-pip python3-flask\
        && pip install -r requirements.txt
        # && flask run
ENTRYPOINT ["flask","run"]