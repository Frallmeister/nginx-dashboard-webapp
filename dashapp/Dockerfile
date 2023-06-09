FROM python:3.11-slim

RUN apt update
RUN apt install nano

# upgrade pip
RUN pip install --upgrade pip

# permissions and nonroot user for tightened security
RUN useradd nonroot
RUN mkdir /home/app/
RUN chown -R nonroot:nonroot /home/app
RUN mkdir -p /var/log/flask-app && touch /var/log/flask-app/flask-app.err.log && touch /var/log/flask-app/flask-app.out.log
RUN chown -R nonroot:nonroot /var/log/flask-app
WORKDIR /home/app

# copy all the files to the container
COPY --chown=nonroot:nonroot . .

# venv
ENV VIRTUAL_ENV=/home/venv

# python setup
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install --upgrade pip
RUN export FLASK_APP=app.py
RUN pip install -r requirements.txt

RUN export FLASK_SERVER_PORT=5000

# define the port number the container should expose
EXPOSE 5000

USER nonroot
CMD ["python", "wsgi.py"]