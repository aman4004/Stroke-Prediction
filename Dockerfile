# base image
FROM python:3.8-slim

# required files
COPY predict.py /usr/app/
COPY SVC_model.p /usr/app/
COPY requirements.txt /usr/app/

# changing working directory
WORKDIR /usr/app/

# installing dependencies
RUN pip install -r requirements.txt

# executing predictor 
CMD ["python", "predict.py" ]
