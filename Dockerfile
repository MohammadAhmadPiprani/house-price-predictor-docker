FROM python:3.11-slim
WORKDIR /app
RUN useradd -m appuser
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
RUN chown -R appuser:appuser /app
EXPOSE 5000
USER appuser
CMD ["python3", "app.py"]


