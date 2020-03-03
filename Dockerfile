FROM python:3.6.10-slim-buster

RUN pip install pipenv
ADD Pipfile .
ADD Pipfile.lock .
RUN pipenv install
ADD models models/
ADD writer writer/
CMD pipenv run python writer/writer.py
