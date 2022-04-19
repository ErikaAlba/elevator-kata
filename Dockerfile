FROM ubuntu:latest

run apt update
run apt install python3 -y

WORKDIR /app

ADD ./ ./

CMD [ "python3", "main.py" ]


