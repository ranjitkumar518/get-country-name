FROM python:3.6.5-alpine
MAINTAINER Ranjit Kumar "ranjitkumarg66@gmail.com"
WORKDIR /app
ADD . /app
RUN pip install -r pre-requirements.txt
CMD ["python","get-county-code.py"]
