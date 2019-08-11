FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y build-essential \
                    python3 \
                    python3-dev \
                    python3-pip

COPY . app
WORKDIR /app

RUN pip3 install -r requirements.txt
RUN ls -a

CMD ["python3", "./manage.py", "runserver", "0.0.0.0:8000"]