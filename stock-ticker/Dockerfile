# Dockerfile, Image, Container
# pulling python from docker hub
FROM python:3.10

# add the file
ADD main.py .

# add dependencies
RUN pip install yfinance pandas redis

# run command
CMD ["python", "./main.py"]