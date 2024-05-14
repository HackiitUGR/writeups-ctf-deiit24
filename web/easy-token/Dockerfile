FROM python:3.10-alpine
WORKDIR /code
#ENV FLASK_APP = easy-jwt.py
ENV FLASK_RUN_HOST=0.0.0.0
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python3", "easy-jwt.py"]
