FROM python:3.12-slim
WORKDIR /app
COPY main.py .
RUN pip install flask --quiet
EXPOSE 8080
CMD ["python3", "main.py"]
