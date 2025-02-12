FROM python:3.8

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY ./app /code/app
#CMD ["uvicorn", "app.main:app", "--reload"]
CMD ["fastapi", "run", "app/main.py", "--port", "80"]
