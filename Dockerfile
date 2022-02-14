FROM python:3.8-slim
COPY . /usr/app
WORKDIR /usr/app
RUN pip install -r requirements.txt
CMD ["python", "predict.py" ]