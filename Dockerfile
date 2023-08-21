FROM python:3.12-rc-alpine
WORKDIR /app
COPY . .
ENV FLASK_APP=app.py
RUN pip install -r requirements.txt
CMD [ "flask", "run", "--host=0.0.0.0", "--port=5000", "--reload"]