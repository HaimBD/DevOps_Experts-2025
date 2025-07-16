FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN mkdir -p /app/logs
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y curl --no-install-recommends
CMD ["python", "script1.py"]