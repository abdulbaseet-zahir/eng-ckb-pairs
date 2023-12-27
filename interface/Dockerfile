# Specify the base image
FROM python:3.9-slim

WORKDIR /interface
COPY requirements.txt .
RUN python3 -m venv venv && \
    ./venv/bin/pip install -r requirements.txt

COPY . .

ENTRYPOINT ["./venv/bin/streamlit", "run", "./app/1_Home.py", "--server.port=8501", "--server.address=0.0.0.0"]
