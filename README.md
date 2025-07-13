# Selenium WebDriver Application

A Python application that uses Selenium WebDriver to automate browser interactions.

## Features

- Automated browser navigation using Selenium WebDriver
- Chrome browser automation with headless mode support
- Docker containerization for easy deployment
- DigitalOcean deployment ready

## Local Development

### Prerequisites

- Python 3.11+
- Chrome browser installed
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd webdriver
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

## Docker Usage

### Build and Run with Docker

1. Build the Docker image:
```bash
docker build -t webdriver-app .
```

2. Run the container:
```bash
docker run --rm webdriver-app
```

### Using Docker Compose

1. Build and run with docker-compose:
```bash
docker-compose up --build
```

2. Run in detached mode:
```bash
docker-compose up -d
```

3. Stop the container:
```bash
docker-compose down
```

## DigitalOcean Deployment Guide

### Prerequisites

- DigitalOcean account
- Docker Hub account (optional, for private repositories)
- SSH key configured on your local machine

### Method 1: Deploy using DigitalOcean App Platform

1. **Prepare your repository:**
   - Push your code to a Git repository (GitHub, GitLab, etc.)
   - Ensure your repository is public or connected to DigitalOcean

2. **Create App on DigitalOcean:**
   - Log in to DigitalOcean
   - Go to Apps → Create App
   - Connect your Git repository
   - Select the repository containing your webdriver app

3. **Configure the App:**
   - **Build Command:** Leave empty (Dockerfile will be used)
   - **Run Command:** Leave empty (CMD in Dockerfile will be used)
   - **Environment Variables:** Add if needed
   - **Resource Allocation:** Choose appropriate plan (Basic or Pro)

4. **Deploy:**
   - Click "Create Resources"
   - Wait for deployment to complete

### Method 2: Deploy using DigitalOcean Droplet

1. **Create a Droplet:**
   - Log in to DigitalOcean
   - Create Droplet → Choose Ubuntu 22.04 LTS
   - Choose plan (Basic or Premium)
   - Add SSH key
   - Create Droplet

2. **Connect to your Droplet:**
```bash
ssh root@your-droplet-ip
```

3. **Install Docker:**
```bash
# Update system
apt update && apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Add user to docker group
usermod -aG docker $USER
```

4. **Clone and deploy your application:**
```bash
# Clone your repository
git clone <your-repo-url>
cd webdriver

# Build and run the Docker image
docker build -t webdriver-app .
docker run -d --name webdriver-container webdriver-app
```

5. **Set up automatic deployment (optional):**
```bash
# Create a deployment script
cat > deploy.sh << 'EOF'
#!/bin/bash
cd /root/webdriver
git pull
docker stop webdriver-container || true
docker rm webdriver-container || true
docker build -t webdriver-app .
docker run -d --name webdriver-container webdriver-app
EOF

chmod +x deploy.sh
```

### Method 3: Using DigitalOcean Container Registry

1. **Create Container Registry:**
   - Go to DigitalOcean → Container Registry
   - Create a new registry

2. **Tag and push your image:**
```bash
# Tag your image
docker tag webdriver-app registry.digitalocean.com/your-registry/webdriver-app:latest

# Push to registry
docker push registry.digitalocean.com/your-registry/webdriver-app:latest
```

3. **Deploy from registry:**
```bash
# Pull and run from registry
docker pull registry.digitalocean.com/your-registry/webdriver-app:latest
docker run -d --name webdriver-container registry.digitalocean.com/your-registry/webdriver-app:latest
```

## Monitoring and Logs

### View Application Logs

```bash
# If using Docker
docker logs webdriver-container

# If using docker-compose
docker-compose logs webdriver-app

# Follow logs in real-time
docker logs -f webdriver-container
```

### Health Checks

Add a simple health check endpoint to your application if needed:

```python
# Add to app.py for web server functionality
from flask import Flask
app = Flask(__name__)

@app.route('/health')
def health():
    return {'status': 'healthy'}, 200
```

## Troubleshooting

### Common Issues

1. **Chrome crashes in container:**
   - Ensure all Chrome flags are set correctly
   - Check if running with sufficient memory

2. **Permission issues:**
   - Ensure Docker is running with proper permissions
   - Check file ownership in mounted volumes

3. **Network connectivity:**
   - Verify firewall settings
   - Check if target URLs are accessible

### Debug Mode

To run in debug mode with visible browser:

```bash
# Modify app.py to set headless=False
# Or run with environment variable
docker run -e CHROME_HEADLESS=false webdriver-app
```

## Security Considerations

- The application runs as a non-root user in the container
- Chrome is configured with security flags
- Consider using secrets management for sensitive data
- Regularly update dependencies and base images

## Cost Optimization

- Use appropriate droplet sizes for your workload
- Consider using DigitalOcean's Basic plans for development
- Monitor resource usage and scale accordingly
- Use container registry for efficient image distribution

## Support

For issues related to:
- **Selenium/WebDriver:** Check Selenium documentation
- **Docker:** Refer to Docker documentation
- **DigitalOcean:** Contact DigitalOcean support 