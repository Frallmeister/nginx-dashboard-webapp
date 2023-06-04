FROM python:3.11-slim

RUN apt update
RUN apt install nano

# upgrade pip
RUN pip install --upgrade pip

WORKDIR /home/app/

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]