FROM python:3.12-rc-alpine
WORKDIR /app
COPY . .
ENV FLASK_APP=app.py
CMD [ "flask", "run" ]