FROM python:3.11

COPY . /kobakLabServerProject

WORKDIR /kobakLabServerProject

EXPOSE 8001

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver"]