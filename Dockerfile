FROM python:3.6.10-slim-buster

RUN pip install pipenv
ADD Pipfile .
ADD Pipfile.lock .
RUN pipenv install
ADD tweetfetch.py .
CMD pipenv run python tweetfetch.py
