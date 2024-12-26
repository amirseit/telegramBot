# Use the official Python image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /app/

# Expose the default bot port (optional for monitoring, etc.)
EXPOSE 5000

# Run the bot
CMD ["python", "bot.py"]
