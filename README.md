# Nginx-Reverse-proxy-
NGINX Reverse Proxy project with Python backend demonstrating real-world web architecture.
# NGINX Reverse Proxy Project

## 📌 Overview
This project demonstrates how to configure NGINX as a reverse proxy to connect a frontend web application with a backend Python server.

---

## 🏗️ Architecture

User → NGINX → Python Backend

- NGINX listens on port 80
- Backend runs on port 3001
- Requests are forwarded using reverse proxy

---

## ⚙️ Technologies Used

- NGINX
- Python (HTTP Server)
- Linux

---

## 📂 Project Structure
---

## 🚀 How to Run

### 1. Start Backend Server

python3 server.py


### 2. Start NGINX

sudo systemctl start nginx


### 3. Access Application

http://localhost


---

## 🔄 Reverse Proxy Config


server {
listen 80;

location /api/ {
    proxy_pass http://127.0.0.1:3001;
}

}


