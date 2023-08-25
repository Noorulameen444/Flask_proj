FROM python:3.11-slim-bullseye
WORKDIR /app
COPY . .
ENV FLASK_APP=/app/src/App/app.py
RUN pip install -r requirements.txt
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000","--reload"]