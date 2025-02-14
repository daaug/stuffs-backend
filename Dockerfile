FROM python:3.8

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
#RUN pip3 install --no-cache-dir -r /code/requirements.txt
RUN pip3 install -r /code/requirements.txt

#COPY ./app /code/app

CMD ["fastapi", "run", "app/main.py", "--port", "80", "--reload"]
