#!/usr/bin/env python3
"""
Day 18: Docker Fundamentals
============================
Duration: 2 hours

Learn Docker - the standard for packaging and deploying applications.
Essential for any data engineering role.

WHY THIS MATTERS:
- "Works on my machine" is solved by Docker
- All modern deployments use containers
- Airflow, dbt, databases - all run in Docker
- This is a must-have skill for data engineers

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

import os
import subprocess
from typing import Dict, List, Optional

# =============================================================================
# DOCKER EXERCISES (Terminal)
# =============================================================================

"""
EXERCISE 1: Docker Installation & Basics (15 min)
==================================================

Install Docker Desktop:
1. Go to https://www.docker.com/products/docker-desktop
2. Download for your OS
3. Install and start Docker Desktop
4. Verify:
   docker --version
   docker run hello-world

If you see "Hello from Docker!", you're ready!


EXERCISE 2: Understanding Images & Containers (15 min)
======================================================

Key concepts:
- IMAGE: A template (like a class in OOP)
- CONTAINER: A running instance (like an object)

Commands to explore:
# See local images
docker images

# Pull an image
docker pull python:3.11-slim

# See running containers
docker ps

# See all containers (including stopped)
docker ps -a

# Run a container
docker run python:3.11-slim python --version

# Run interactive container
docker run -it python:3.11-slim bash
# (type 'exit' to leave)


EXERCISE 3: Your First Dockerfile (25 min)
==========================================

Create a simple Python application:

1. Create a project folder:
   mkdir docker-practice && cd docker-practice

2. Create app.py:
   # app.py
   def main():
       print("Hello from Docker!")
       print("This is a containerized Python application.")
       
   if __name__ == "__main__":
       main()

3. Create Dockerfile:
   # Dockerfile
   FROM python:3.11-slim
   
   WORKDIR /app
   
   COPY app.py .
   
   CMD ["python", "app.py"]

4. Build the image:
   docker build -t my-python-app .

5. Run it:
   docker run my-python-app


EXERCISE 4: Dockerfile with Dependencies (25 min)
==================================================

Create a more realistic application:

1. Create requirements.txt:
   requests==2.31.0
   python-dotenv==1.0.0

2. Create app.py:
   import requests
   import os
   from dotenv import load_dotenv
   
   load_dotenv()
   
   def main():
       api_key = os.getenv("API_KEY", "demo")
       print(f"Running with API key: {api_key[:4]}...")
       
       response = requests.get("https://httpbin.org/get")
       print(f"Status: {response.status_code}")
   
   if __name__ == "__main__":
       main()

3. Create improved Dockerfile:
   # Dockerfile
   FROM python:3.11-slim
   
   # Set working directory
   WORKDIR /app
   
   # Copy and install dependencies first (better layer caching)
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   
   # Copy application code
   COPY app.py .
   
   # Environment variable with default
   ENV API_KEY=demo
   
   # Run the application
   CMD ["python", "app.py"]

4. Build and run:
   docker build -t my-api-app .
   docker run my-api-app
   
   # With custom environment variable:
   docker run -e API_KEY=my-secret-key my-api-app


EXERCISE 5: Volumes - Persisting Data (20 min)
===============================================

Containers are ephemeral. Volumes persist data.

1. Create a data processing script:
   # process.py
   import os
   import json
   from datetime import datetime
   
   OUTPUT_DIR = "/data/output"
   
   def main():
       os.makedirs(OUTPUT_DIR, exist_ok=True)
       
       result = {
           "processed_at": datetime.now().isoformat(),
           "status": "success",
           "records": 100
       }
       
       output_path = f"{OUTPUT_DIR}/result.json"
       with open(output_path, "w") as f:
           json.dump(result, f, indent=2)
       
       print(f"Wrote result to {output_path}")
   
   if __name__ == "__main__":
       main()

2. Run with a volume:
   docker build -t data-processor .
   
   # Mount local folder to container's /data/output
   docker run -v $(pwd)/output:/data/output data-processor
   
   # Check your local output folder
   cat output/result.json


EXERCISE 6: Docker Networking (15 min)
======================================

Containers can expose ports:

1. Create a simple web server:
   # server.py
   from http.server import HTTPServer, SimpleHTTPRequestHandler
   import json
   
   class Handler(SimpleHTTPRequestHandler):
       def do_GET(self):
           self.send_response(200)
           self.send_header("Content-type", "application/json")
           self.end_headers()
           response = {"message": "Hello from Docker!", "path": self.path}
           self.wfile.write(json.dumps(response).encode())
   
   if __name__ == "__main__":
       server = HTTPServer(("0.0.0.0", 8080), Handler)
       print("Server running on port 8080...")
       server.serve_forever()

2. Dockerfile:
   FROM python:3.11-slim
   WORKDIR /app
   COPY server.py .
   EXPOSE 8080
   CMD ["python", "server.py"]

3. Run with port mapping:
   docker build -t my-server .
   docker run -p 8080:8080 my-server
   
   # In another terminal:
   curl http://localhost:8080/test


EXERCISE 7: Docker Compose - Multiple Containers (20 min)
=========================================================

Docker Compose manages multi-container applications.

1. Create docker-compose.yml:
   version: '3.8'
   
   services:
     app:
       build: .
       ports:
         - "8080:8080"
       environment:
         - API_KEY=my-key
       volumes:
         - ./data:/data
       depends_on:
         - db
     
     db:
       image: postgres:15
       environment:
         POSTGRES_USER: user
         POSTGRES_PASSWORD: password
         POSTGRES_DB: mydb
       volumes:
         - postgres_data:/var/lib/postgresql/data
       ports:
         - "5432:5432"
   
   volumes:
     postgres_data:

2. Run with Compose:
   docker-compose up
   
   # Detached (background):
   docker-compose up -d
   
   # See logs:
   docker-compose logs -f
   
   # Stop:
   docker-compose down


EXERCISE 8: Best Practices (5 min)
==================================

1. Use specific image tags (python:3.11-slim, not python:latest)
2. Order Dockerfile commands for cache efficiency
3. Use .dockerignore to exclude unnecessary files
4. Don't run as root in production
5. Keep images small (use slim/alpine bases)

Create .dockerignore:
__pycache__
*.pyc
.git
.env
*.md
.pytest_cache
venv/
"""

# =============================================================================
# DOCKERFILE TEMPLATES
# =============================================================================

DOCKERFILE_TEMPLATES = {
    "basic_python": '''FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
''',

    "data_pipeline": '''FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \\
    gcc \\
    libpq-dev \\
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY src/ ./src/
COPY config/ ./config/

# Set environment
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["python", "-m", "src.main"]
''',

    "airflow_task": '''FROM apache/airflow:2.7.0-python3.11

USER root
RUN apt-get update && apt-get install -y \\
    gcc \\
    && rm -rf /var/lib/apt/lists/*

USER airflow

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY dags/ /opt/airflow/dags/
COPY plugins/ /opt/airflow/plugins/
''',

    "multi_stage": '''# Build stage
FROM python:3.11-slim as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Production stage
FROM python:3.11-slim

WORKDIR /app
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY . .

CMD ["python", "main.py"]
'''
}


def print_dockerfile_template(name: str) -> None:
    """Print a Dockerfile template."""
    if name not in DOCKERFILE_TEMPLATES:
        print(f"Unknown template. Available: {', '.join(DOCKERFILE_TEMPLATES.keys())}")
        return
    
    print(f"# Dockerfile template: {name}")
    print("-" * 40)
    print(DOCKERFILE_TEMPLATES[name])


# =============================================================================
# DOCKER HELPERS
# =============================================================================

def check_docker_installed() -> bool:
    """Check if Docker is installed and running."""
    try:
        result = subprocess.run(
            ["docker", "--version"],
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except FileNotFoundError:
        return False


def get_docker_info() -> Optional[Dict]:
    """Get Docker system information."""
    try:
        result = subprocess.run(
            ["docker", "info", "--format", "{{json .}}"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            import json
            return json.loads(result.stdout)
        return None
    except:
        return None


def list_images() -> List[Dict]:
    """List local Docker images."""
    try:
        result = subprocess.run(
            ["docker", "images", "--format", "{{.Repository}}:{{.Tag}}\t{{.Size}}\t{{.CreatedSince}}"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            images = []
            for line in result.stdout.strip().split("\n"):
                if line:
                    parts = line.split("\t")
                    images.append({
                        "name": parts[0],
                        "size": parts[1] if len(parts) > 1 else "unknown",
                        "created": parts[2] if len(parts) > 2 else "unknown"
                    })
            return images
        return []
    except:
        return []


def list_containers(all_containers: bool = False) -> List[Dict]:
    """List Docker containers."""
    try:
        cmd = ["docker", "ps", "--format", "{{.Names}}\t{{.Image}}\t{{.Status}}"]
        if all_containers:
            cmd.insert(2, "-a")
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            containers = []
            for line in result.stdout.strip().split("\n"):
                if line:
                    parts = line.split("\t")
                    containers.append({
                        "name": parts[0],
                        "image": parts[1] if len(parts) > 1 else "unknown",
                        "status": parts[2] if len(parts) > 2 else "unknown"
                    })
            return containers
        return []
    except:
        return []


# =============================================================================
# DOCKER QUIZ
# =============================================================================

def docker_quiz() -> None:
    """Test your Docker knowledge."""
    questions = [
        {
            "q": "What's the difference between an image and a container?",
            "options": [
                "No difference",
                "Image is template, container is running instance",
                "Container is template, image is running instance",
                "Images run in containers"
            ],
            "answer": 1,
            "explanation": "Image = template/blueprint. Container = running instance of an image."
        },
        {
            "q": "Which command runs a container in the background?",
            "options": [
                "docker run --background",
                "docker run -d",
                "docker run --detach",
                "Both B and C"
            ],
            "answer": 3,
            "explanation": "-d and --detach are the same. They run the container detached (background)."
        },
        {
            "q": "What does -v host_path:container_path do?",
            "options": [
                "Sets volume verbosity",
                "Mounts host directory into container",
                "Creates a virtual network",
                "Validates the path"
            ],
            "answer": 1,
            "explanation": "-v mounts a volume - maps a host path to a container path for data persistence."
        },
        {
            "q": "Why put COPY requirements.txt before COPY . . in a Dockerfile?",
            "options": [
                "It doesn't matter",
                "Requirements must be first",
                "For better layer caching - dependencies change less often",
                "Docker requires this order"
            ],
            "answer": 2,
            "explanation": "Docker caches layers. Dependencies change rarely, so install them first to cache that layer."
        },
        {
            "q": "What is docker-compose used for?",
            "options": [
                "Composing Dockerfiles",
                "Managing multi-container applications",
                "Compressing Docker images",
                "Writing Docker documentation"
            ],
            "answer": 1,
            "explanation": "Docker Compose defines and runs multi-container Docker applications with a YAML file."
        }
    ]
    
    print("=" * 60)
    print("DOCKER KNOWLEDGE QUIZ")
    print("=" * 60 + "\n")
    
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['q']}")
        for j, opt in enumerate(q['options']):
            print(f"  {j+1}. {opt}")
        
        try:
            answer = int(input("Your answer (1-4): ")) - 1
            if answer == q['answer']:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Incorrect. {q['explanation']}\n")
        except:
            print(f"Invalid input. {q['explanation']}\n")
    
    print("=" * 60)
    print(f"Score: {score}/{len(questions)}")
    print("=" * 60)


# =============================================================================
# Verification
# =============================================================================

def verify_docker_setup() -> None:
    """Verify Docker installation and setup."""
    print("=" * 60)
    print("DOCKER SETUP VERIFICATION")
    print("=" * 60 + "\n")
    
    if not check_docker_installed():
        print("❌ Docker not installed or not in PATH")
        print("   Install from: https://www.docker.com/products/docker-desktop")
        return
    
    print("✅ Docker is installed")
    
    # Get version
    result = subprocess.run(["docker", "--version"], capture_output=True, text=True)
    print(f"   Version: {result.stdout.strip()}")
    
    # Check if daemon is running
    info = get_docker_info()
    if info:
        print("✅ Docker daemon is running")
    else:
        print("❌ Docker daemon is not running. Start Docker Desktop.")
        return
    
    # List images
    images = list_images()
    print(f"\n📦 Local images: {len(images)}")
    for img in images[:5]:
        print(f"   - {img['name']} ({img['size']})")
    
    # List containers
    containers = list_containers(all_containers=True)
    running = [c for c in containers if "Up" in c.get("status", "")]
    print(f"\n🐳 Containers: {len(running)} running, {len(containers)} total")
    
    print("\n" + "-" * 40)
    print("Checklist:")
    print("[ ] Docker Desktop installed and running")
    print("[ ] Ran 'docker run hello-world' successfully")
    print("[ ] Built your first image")
    print("[ ] Ran container with volume mount")
    print("[ ] Ran container with port mapping")
    print("-" * 40)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "verify":
            verify_docker_setup()
        elif cmd == "quiz":
            docker_quiz()
        elif cmd == "template":
            name = sys.argv[2] if len(sys.argv) > 2 else "basic_python"
            print_dockerfile_template(name)
        elif cmd == "templates":
            print("Available Dockerfile templates:")
            for name in DOCKERFILE_TEMPLATES:
                print(f"  - {name}")
    else:
        print("Day 18: Docker Fundamentals")
        print("=" * 40)
        print("\nThis is a Docker-focused day.")
        print("Follow the exercises in terminal.")
        print("\nCommands:")
        print("  python day18_docker_fundamentals.py verify    - Verify Docker setup")
        print("  python day18_docker_fundamentals.py quiz      - Take the Docker quiz")
        print("  python day18_docker_fundamentals.py templates - List Dockerfile templates")
        print("  python day18_docker_fundamentals.py template <name> - Show a template")
