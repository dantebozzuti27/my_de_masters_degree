#!/usr/bin/env python3
"""
Day 18: Docker Fundamentals - Complete Beginner to Working Knowledge
=====================================================================
Duration: 3-4 hours total

Today you'll learn Docker from absolute scratch. By the end, you'll understand
containers, build your own images, and run applications in Docker.

DAILY STRUCTURE:
├── LEARN (60-90 min): Videos + Reading
├── BUILD (2-2.5 hrs): Hands-on coding
└── REVIEW (15-30 min): Document + commit

PREREQUISITES: 
- Docker Desktop installed (you did this after Day 14)
- Basic command line skills

COMPLETION: Delete the marker below when you've finished all exercises.
"""

# YOUR CODE HERE - DELETE THIS LINE WHEN EXERCISES COMPLETE

# =============================================================================
# PART 1: LEARN (60-90 minutes)
# =============================================================================
"""
WHAT IS DOCKER?
===============
Docker is a tool that packages applications with everything they need to run.

THE PROBLEM DOCKER SOLVES:
--------------------------
"It works on my machine!" - the most dreaded phrase in software.

Your code might work on your laptop but fail on:
- Your coworker's machine (different Python version)
- The test server (missing a library)
- Production (different operating system)

Docker fixes this by packaging:
- Your code
- All dependencies (Python, libraries, etc.)
- Environment configuration
- Even parts of the operating system

Into a single, portable unit called a CONTAINER.


KEY CONCEPTS (memorize these):
==============================

1. IMAGE
   - A blueprint/template for creating containers
   - Like a class in Python
   - Read-only
   - Built from a Dockerfile
   - Example: "python:3.11-slim" is an image

2. CONTAINER
   - A running instance of an image
   - Like an object created from a class
   - Isolated environment
   - Can create many containers from one image
   - Example: Running your data pipeline

3. DOCKERFILE
   - A text file with instructions to build an image
   - Lists what base image to use, what to install, etc.
   - Like a recipe

4. REGISTRY
   - Where images are stored and shared
   - Docker Hub is the main public registry
   - Like GitHub but for Docker images

5. LAYER
   - Docker images are built in layers
   - Each instruction creates a layer
   - Layers are cached (faster rebuilds)


ANALOGY:
========
Think of it like shipping containers on cargo ships:

- Before containers: Each product shipped differently
- After containers: Standard boxes that work everywhere

Docker does the same for software:
- Before Docker: Install dependencies manually on each machine
- After Docker: Same container runs everywhere


WHY DOCKER FOR DATA ENGINEERING?
================================
- Airflow runs in Docker
- dbt runs in Docker
- Most databases run in Docker for development
- Production pipelines are containerized
- "Runs on my machine" never happens again


LEARNING RESOURCES (Pick 1-2, spend 60-90 min):
===============================================

VIDEO (Choose one):
- "Docker Tutorial for Beginners" - TechWorld with Nana (1 hour)
  https://www.youtube.com/watch?v=3c-iBn73dDE
  HIGHLY RECOMMENDED - Best intro to Docker
  
- "Docker in 100 Seconds + Tutorial" - Fireship (13 min for basics)
  https://www.youtube.com/watch?v=Gjnup-PuquQ

READING:
- Docker Getting Started Guide
  https://docs.docker.com/get-started/
  
- "Fundamentals of Data Engineering" - pages on containerization
  If you have the book, search for "Docker" sections


AFTER LEARNING, answer these:
1. What's the difference between an image and a container?
2. Why are Docker layers useful?
3. What does "containerization" solve?

When done with LEARN, move to BUILD.
"""


# =============================================================================
# PART 2: BUILD (2-2.5 hours)
# =============================================================================

"""
EXERCISE 1: VERIFY DOCKER INSTALLATION (5 min)
==============================================

Run these commands in your terminal:

    docker --version
    docker run hello-world

The hello-world test should print a message explaining Docker works.

If it fails, ensure Docker Desktop is running (check your menu bar).
"""


"""
EXERCISE 2: UNDERSTAND BASIC COMMANDS (15 min)
==============================================

Let's learn the essential Docker commands.

LIST IMAGES (images on your machine):

    docker images
    
You should see "hello-world" from the test.

LIST CONTAINERS:

    docker ps        # Running containers only
    docker ps -a     # All containers (including stopped)

PULL AN IMAGE (download from Docker Hub):

    docker pull python:3.11-slim

This downloads the official Python 3.11 image (slim = smaller version).

RUN A CONTAINER:

    docker run python:3.11-slim python --version

This:
1. Creates a container from the python:3.11-slim image
2. Runs "python --version" inside it
3. Exits when done

RUN INTERACTIVE CONTAINER:

    docker run -it python:3.11-slim bash

The flags:
- -i = interactive (keep STDIN open)
- -t = allocate a pseudo-TTY (terminal)

You're now INSIDE the container! Try:
    python --version
    pip list
    exit

REMOVE STOPPED CONTAINERS (cleanup):

    docker container prune
    
REMOVE UNUSED IMAGES (cleanup):

    docker image prune
"""


"""
EXERCISE 3: YOUR FIRST DOCKERFILE (30 min)
==========================================

Let's build your own Docker image.

STEP 1: Create a project folder

    mkdir -p ~/docker-practice
    cd ~/docker-practice

STEP 2: Create a simple Python script

Create file: ~/docker-practice/app.py
"""

# This is what app.py should contain:
APP_PY_CONTENT = '''
import os
from datetime import datetime

def main():
    print("=" * 50)
    print("HELLO FROM DOCKER!")
    print("=" * 50)
    print(f"Current time: {datetime.now()}")
    print(f"Python version: {os.sys.version}")
    print(f"Hostname: {os.uname().nodename}")
    print(f"Working directory: {os.getcwd()}")
    print("=" * 50)

if __name__ == "__main__":
    main()
'''

"""
Create the file:

    cat > ~/docker-practice/app.py << 'EOF'
import os
from datetime import datetime

def main():
    print("=" * 50)
    print("HELLO FROM DOCKER!")
    print("=" * 50)
    print(f"Current time: {datetime.now()}")
    print(f"Python version: {os.sys.version}")
    print(f"Hostname: {os.uname().nodename}")
    print(f"Working directory: {os.getcwd()}")
    print("=" * 50)

if __name__ == "__main__":
    main()
EOF


STEP 3: Create a Dockerfile

A Dockerfile is a recipe for building an image.

    cat > ~/docker-practice/Dockerfile << 'EOF'
# Base image - start with official Python
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy our code into the container
COPY app.py .

# Command to run when container starts
CMD ["python", "app.py"]
EOF


Let's break down each line:

FROM python:3.11-slim
    - Start with this base image
    - It already has Python installed
    - "slim" = smaller size (no GUI, dev tools)

WORKDIR /app
    - Create /app directory and cd into it
    - Like: mkdir /app && cd /app

COPY app.py .
    - Copy app.py from your machine into the container
    - The "." means "current directory" (/app)

CMD ["python", "app.py"]
    - The command to run when container starts
    - This runs: python app.py


STEP 4: Build the image

    cd ~/docker-practice
    docker build -t my-python-app .

The flags:
- -t my-python-app = name (tag) the image
- . = build from current directory (where Dockerfile is)

Watch the output - you'll see each layer being created.


STEP 5: Run your container

    docker run my-python-app

You should see the output from your Python script!


STEP 6: Verify the image exists

    docker images | grep my-python-app
"""


"""
EXERCISE 4: UNDERSTANDING LAYERS (20 min)
=========================================

Docker images are built in layers. This is important for efficiency.

STEP 1: Create a more complex Dockerfile

    cat > ~/docker-practice/Dockerfile << 'EOF'
FROM python:3.11-slim

WORKDIR /app

# Layer 1: Install system dependencies
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Layer 2: Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Layer 3: Copy application code
COPY app.py .

CMD ["python", "app.py"]
EOF

STEP 2: Create requirements.txt

    cat > ~/docker-practice/requirements.txt << 'EOF'
requests==2.31.0
EOF

STEP 3: Rebuild

    docker build -t my-python-app .

Notice Docker downloads and installs requests.

STEP 4: Modify app.py slightly

    echo "# Modified" >> ~/docker-practice/app.py

STEP 5: Rebuild again

    docker build -t my-python-app .

Notice it says "CACHED" for the pip install layer!
Docker only rebuilds layers that changed.

WHY THIS MATTERS:
- Dependencies rarely change
- Code changes frequently
- Put things that change LEAST at the TOP of Dockerfile
- Put things that change MOST at the BOTTOM
- This makes builds much faster
"""


"""
EXERCISE 5: ENVIRONMENT VARIABLES (20 min)
==========================================

Containers should be configured via environment variables, not hardcoded values.

STEP 1: Update app.py to use environment variables

    cat > ~/docker-practice/app.py << 'EOF'
import os
from datetime import datetime

def main():
    # Get environment variables with defaults
    app_name = os.getenv("APP_NAME", "My App")
    environment = os.getenv("ENVIRONMENT", "development")
    debug = os.getenv("DEBUG", "false").lower() == "true"
    
    print("=" * 50)
    print(f"Application: {app_name}")
    print(f"Environment: {environment}")
    print(f"Debug mode: {debug}")
    print(f"Time: {datetime.now()}")
    print("=" * 50)
    
    if debug:
        print("\nDEBUG INFO:")
        for key, value in sorted(os.environ.items()):
            print(f"  {key}={value}")

if __name__ == "__main__":
    main()
EOF

STEP 2: Rebuild

    docker build -t my-python-app .

STEP 3: Run with different environments

    # Default values
    docker run my-python-app
    
    # Override with -e flag
    docker run -e APP_NAME="Stock Pipeline" -e ENVIRONMENT="production" my-python-app
    
    # Enable debug mode
    docker run -e DEBUG=true my-python-app

This is how production systems work - same image, different config.
"""


"""
EXERCISE 6: VOLUMES - PERSISTENT DATA (25 min)
==============================================

By default, data inside containers is LOST when the container stops.
Volumes let you persist data.

STEP 1: See the problem

    # Run container and create a file
    docker run -it python:3.11-slim bash
    
    # Inside container:
    echo "important data" > /tmp/mydata.txt
    cat /tmp/mydata.txt
    exit
    
    # Run a new container
    docker run -it python:3.11-slim bash
    
    # Inside container:
    cat /tmp/mydata.txt  # FILE IS GONE!
    exit

STEP 2: Use a volume to persist data

    # Create a directory on your machine
    mkdir -p ~/docker-data
    
    # Run container with volume mounted
    docker run -it -v ~/docker-data:/data python:3.11-slim bash
    
    # Inside container:
    echo "persistent data" > /data/mydata.txt
    exit
    
    # Check on your machine
    cat ~/docker-data/mydata.txt  # Data persists!
    
    # Run new container with same volume
    docker run -it -v ~/docker-data:/data python:3.11-slim bash
    
    # Inside container:
    cat /data/mydata.txt  # Data is there!
    exit

The -v flag syntax:
    -v /host/path:/container/path
    
This "mounts" a folder from your machine into the container.

USE CASES:
- Database data (PostgreSQL stores files)
- Log files
- Input/output files for data pipelines
"""


"""
EXERCISE 7: PORT MAPPING (20 min)
=================================

Containers are isolated - their ports aren't accessible by default.
Port mapping exposes container ports to your machine.

STEP 1: Create a simple web server

    cat > ~/docker-practice/server.py << 'EOF'
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from datetime import datetime

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        response = {
            "message": "Hello from Docker!",
            "time": datetime.now().isoformat(),
            "path": self.path
        }
        
        self.wfile.write(json.dumps(response).encode())
        print(f"Handled request: {self.path}")

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', 8000), Handler)
    print("Server running on port 8000...")
    server.serve_forever()
EOF

STEP 2: Update Dockerfile

    cat > ~/docker-practice/Dockerfile << 'EOF'
FROM python:3.11-slim

WORKDIR /app

COPY server.py .

# Document that container uses port 8000
EXPOSE 8000

CMD ["python", "server.py"]
EOF

STEP 3: Build and run with port mapping

    docker build -t my-server .
    docker run -p 8080:8000 my-server

The -p flag syntax:
    -p HOST_PORT:CONTAINER_PORT
    
Now port 8000 inside the container is accessible as port 8080 on your machine.

STEP 4: Test it (in another terminal)

    curl http://localhost:8080
    curl http://localhost:8080/users

STEP 5: Stop the container

    # In the terminal running Docker, press Ctrl+C
    # Or in another terminal:
    docker ps  # Get container ID
    docker stop <container_id>
"""


"""
EXERCISE 8: BUILD A DATA PIPELINE IMAGE (45 min)
================================================

Let's build a production-style data pipeline Docker image.

STEP 1: Create project structure

    mkdir -p ~/docker-pipeline/src
    cd ~/docker-pipeline

STEP 2: Create the pipeline code

    cat > ~/docker-pipeline/src/pipeline.py << 'EOF'
import os
import json
import requests
from datetime import datetime, timezone

def main():
    print("=" * 60)
    print("DATA PIPELINE - DOCKER EDITION")
    print("=" * 60)
    
    # Configuration from environment
    api_url = os.getenv("API_URL", "https://jsonplaceholder.typicode.com/users")
    output_dir = os.getenv("OUTPUT_DIR", "/data/output")
    
    print(f"API URL: {api_url}")
    print(f"Output directory: {output_dir}")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Fetch data
    print("\n📥 Fetching data...")
    response = requests.get(api_url, timeout=30)
    response.raise_for_status()
    data = response.json()
    print(f"   Fetched {len(data)} records")
    
    # Add metadata
    print("🏷️  Adding metadata...")
    for record in data:
        record['_ingested_at'] = datetime.now(timezone.utc).isoformat()
        record['_source'] = api_url
    
    # Save to file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"users_{timestamp}.json")
    
    print(f"💾 Saving to {output_file}...")
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"\n✅ Pipeline complete! {len(data)} records saved")
    print("=" * 60)

if __name__ == "__main__":
    main()
EOF

STEP 3: Create requirements.txt

    cat > ~/docker-pipeline/requirements.txt << 'EOF'
requests==2.31.0
EOF

STEP 4: Create Dockerfile (production-style)

    cat > ~/docker-pipeline/Dockerfile << 'EOF'
# Use specific Python version for reproducibility
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash pipeline

# Set working directory
WORKDIR /app

# Install dependencies first (better layer caching)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY src/ ./src/

# Change ownership to non-root user
RUN chown -R pipeline:pipeline /app

# Switch to non-root user
USER pipeline

# Create data directory
RUN mkdir -p /app/data/output

# Default command
CMD ["python", "src/pipeline.py"]
EOF

STEP 5: Build the image

    cd ~/docker-pipeline
    docker build -t data-pipeline .

STEP 6: Run the pipeline

    # Run with default settings
    docker run data-pipeline
    
    # Run with custom API and output volume
    docker run -v ~/docker-data:/app/data/output data-pipeline
    
    # Check the output
    ls ~/docker-data/
    cat ~/docker-data/users_*.json | head -50

STEP 7: Run with different API endpoint

    docker run \
        -e API_URL="https://jsonplaceholder.typicode.com/posts" \
        -v ~/docker-data:/app/data/output \
        data-pipeline
    
    ls ~/docker-data/
"""


"""
EXERCISE 9: .dockerignore (10 min)
==================================

Like .gitignore, but for Docker. Prevents copying unnecessary files.

    cat > ~/docker-pipeline/.dockerignore << 'EOF'
# Git
.git
.gitignore

# Python
__pycache__
*.py[cod]
*$py.class
.Python
*.so
.mypy_cache
.pytest_cache

# Virtual environments
venv
.venv
ENV

# IDE
.idea
.vscode
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Docker
Dockerfile
docker-compose.yml
.docker

# Data files (don't include in image)
data/
*.json
*.csv
EOF

This makes builds faster and images smaller.
"""


"""
EXERCISE 10: DOCKER BEST PRACTICES CHECKLIST
============================================

Review this checklist for your Dockerfiles:

[ ] Use specific base image tags (python:3.11-slim, not python:latest)
[ ] Put least-changing layers at the top
[ ] Combine RUN commands with && to reduce layers
[ ] Use .dockerignore to exclude unnecessary files
[ ] Don't run as root in production (USER instruction)
[ ] Set environment variables with ENV
[ ] Document exposed ports with EXPOSE
[ ] Use COPY instead of ADD (more explicit)
[ ] Remove package manager caches (apt-get clean)
[ ] Use multi-stage builds for compiled languages
"""


# =============================================================================
# PART 3: REVIEW (15-30 min)
# =============================================================================

"""
REVIEW CHECKLIST:
=================

Commands - can you do these without looking?
[ ] docker pull <image>
[ ] docker run <image>
[ ] docker run -it <image> bash
[ ] docker run -e VAR=value <image>
[ ] docker run -v /host:/container <image>
[ ] docker run -p HOST:CONTAINER <image>
[ ] docker build -t name .
[ ] docker ps / docker ps -a
[ ] docker images
[ ] docker stop <id>

Dockerfile - can you write these instructions?
[ ] FROM
[ ] WORKDIR
[ ] COPY
[ ] RUN
[ ] ENV
[ ] EXPOSE
[ ] CMD

Concepts - can you explain these?
[ ] What's the difference between an image and a container?
[ ] What happens when you change code and rebuild?
[ ] Why order Dockerfile instructions by change frequency?
[ ] What does the -v flag do?
[ ] What does the -p flag do?

KNOWLEDGE CHECK QUESTIONS:
==========================

1. Your Dockerfile has: COPY requirements.txt then RUN pip install, 
   then COPY app.py. You change app.py. What gets rebuilt?

2. You run a container with a database. The container stops.
   Is the data lost? How do you prevent this?

3. Your container runs a web server on port 5000. How do you
   access it from your browser at localhost:3000?

Write your answers before moving on.


COMMIT YOUR WORK:
=================

    cd ~/cursor/Projects/Business/SDE_PATH/sde-tracker
    git add -A
    git commit -m "Complete Day 18: Docker Fundamentals"
    git push


WHAT'S NEXT:
============
Day 19: Docker for Data Engineering
- Multi-stage builds
- Docker Compose basics
- Running databases in Docker
- Local development environments
"""


if __name__ == "__main__":
    print("Day 18: Docker Fundamentals")
    print("=" * 50)
    print("\nThis lesson is primarily terminal-based.")
    print("Follow the exercises in the comments above.")
    print("\nKey commands to practice:")
    print("  docker run hello-world")
    print("  docker build -t myapp .")
    print("  docker run -it myapp bash")
    print("  docker run -v ~/data:/data myapp")
    print("  docker run -p 8080:8000 myapp")
