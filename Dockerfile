FROM python:3.9-slim-buster

WORKDIR /myportfolio

# Copy requirements first to leverage Docker layer caching
# This layer is only rebuilt when requirements.txt changes
COPY requirements.txt .

RUN pip3 install -r requirements.txt

# Copy the rest of the project files
COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000
