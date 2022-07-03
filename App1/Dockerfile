FROM ubuntu:20.04
WORKDIR /code
COPY . .
EXPOSE 3001
RUN apt -y update && apt install nano &&apt install -y python3-pip && pip3 install flask
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
ENTRYPOINT ["flask", "run"]