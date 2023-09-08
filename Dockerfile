FROM python:3
WORKDIR /myapp
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
