# 🏠 House Price Predictor

A Machine Learning web application that predicts house prices based on user-provided features.

This project was originally built with **Python and Flask** and has been containerized using **Docker**. **NGINX** is used as a reverse proxy to forward incoming HTTP requests to the Flask application.

## 🏗️ Architecture

```text
                Browser
                   │
                   │ HTTP :8080
                   ▼
          ┌─────────────────┐
          │      NGINX      │
          │  Container :80  │
          └────────┬────────┘
                   │
                   │ web-app:5000
                   ▼
          ┌─────────────────┐
          │  Flask Web App  │
          │ Container :5000 │
          └────────┬────────┘
                   │
                   ▼
                model.pkl
                   │
                   ▼
          House Price Prediction
```

## 🚀 Technologies Used

* Python
* Flask
* NumPy
* Scikit-learn
* Pickle
* HTML/CSS
* Docker
* Docker Compose
* NGINX

## 📁 Project Structure

```text
House_Price_Predictor/
│
├── app.py
├── model.py
├── model.pkl
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
│
├── nginx/
│   ├── Dockerfile
│   └── nginx.conf
│
├── Data/
├── static/
├── templates/
│
└── README.md
```

## 🐳 Docker Setup

The application consists of two Docker containers:

### Flask Application

The Flask application runs inside the container on:

```text
0.0.0.0:5000
```

The application listens on all container network interfaces so that NGINX can communicate with it through the Docker network.

### NGINX

NGINX listens inside the container on:

```text
0.0.0.0:80
```

The NGINX container's port `80` is mapped to port `8080` on the host machine.

Therefore, the application is accessed from the browser using:

```text
http://localhost:8080
```

## ⚙️ NGINX Reverse Proxy

NGINX acts as a reverse proxy between the browser and the Flask application.

Incoming requests are forwarded to the Flask service:

```nginx
location / {
    proxy_pass http://web-app:5000;
}
```

Docker Compose provides an internal network, allowing NGINX to communicate with the Flask container using the service name `web-app`.

The communication flow is:

```text
localhost:8080
      ↓
NGINX:80
      ↓
web-app:5000
      ↓
Flask Application
```

## 📦 Requirements

The project uses a pinned version of Scikit-learn to maintain compatibility with the serialized machine learning model:

```text
scikit-learn==1.4.1.post1
```

Pinning dependency versions helps prevent compatibility problems between the environment used to create the model and the Docker runtime environment.

## ▶️ Run the Project with Docker

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd House_Price_Predictor
```

### 2. Build and start the containers

```bash
docker compose up -d --build
```

### 3. Check running containers

```bash
docker compose ps
```

### 4. Open the application

Open your browser and visit:

```text
http://localhost:8080
```

NGINX receives the request on port `80` inside the container and forwards it to the Flask application running on port `5000`.

## 🛑 Stop the Application

To stop and remove the containers:

```bash
docker compose down
```

To rebuild the images after making changes:

```bash
docker compose up -d --build
```

## 🔍 Troubleshooting

### Check container status

```bash
docker compose ps
```

### View Flask application logs

```bash
docker compose logs web-app
```

### View NGINX logs

```bash
docker compose logs nginx
```

### Follow logs in real time

```bash
docker compose logs -f
```

## 🧠 Important Docker Lessons

During the Dockerization process, the project demonstrated two important containerization concepts.

### 1. Container Networking

The Flask application originally listened on:

```text
127.0.0.1:5000
```

This worked when running the application directly on the host machine, but it prevented NGINX running in a separate Docker container from reaching the Flask application.

The Flask application was therefore configured to listen on:

```text
0.0.0.0:5000
```

This allowed communication between the NGINX and Flask containers through the Docker network.

### 2. Dependency Compatibility

The machine learning model was created and tested using a specific Scikit-learn version.

The Docker container initially used a different version, which caused the following error when loading the serialized model:

```text
AttributeError: 'LinearRegression' object has no attribute 'positive'
```

The issue was caused by a compatibility difference between the Scikit-learn version used to create the model and the version installed inside the Docker container.

The issue was resolved by using the compatible version:

```text
scikit-learn==1.4.1.post1
```

This demonstrates the importance of **dependency version pinning and reproducible environments** when containerizing applications.

## 🎯 Project Goals

* Run a Flask ML application inside Docker
* Create a reproducible Python environment
* Use Docker Compose to manage multiple services
* Configure NGINX as a reverse proxy
* Establish communication between Docker containers
* Handle dependency compatibility
* Practice container troubleshooting and debugging
* Understand Docker networking between services

## 👨‍💻 Author

**Muhammad Ahmed**



       
