# Dockerfile: Defines the container environment

# Use a specific, stable Python image as the base
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
# NOTE: If you don't have a requirements.txt, you must create one 
# with 'google-adk' and 'pyyaml' listed.
COPY requirements.txt .

# Install dependencies (use the non-cache flag for clean builds)
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
# This includes agent.py, tools.py, run_justice_map.py, etc.
COPY . .

# Set the environment variable for the API key to be passed at runtime
# (This variable must be set when the container is deployed)
ENV GEMINI_API_KEY="placeholder"

# Command to run your agent system's entry point when the container starts
# Replace 'main:app' with your actual agent entry command if you were using FastAPI,
# but for a simple script, we run the Python file that starts the AgentClient.
CMD ["python", "run_justice_map.py"]
