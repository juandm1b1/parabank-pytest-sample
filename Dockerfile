# 1. Official Playwright base image (Includes Python and browsers pre-installed)
FROM mcr.microsoft.com/playwright/python:v1.50.0-jammy

# 2. Install Java and Allure CLI (required to generate the report)
USER root
RUN apt-get update && \
    apt-get install -y openjdk-11-jre-headless wget unzip && \
    wget https://github.com/allure-framework/allure2/releases/download/2.30.0/allure-2.30.0.tgz && \
    tar -zxvf allure-2.30.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.30.0/bin/allure /usr/bin/allure && \
    rm allure-2.30.0.tgz && \
    rm -rf /var/lib/apt/lists/*

# 3. Set working directory
WORKDIR /app

# 4. Copy and install Python dependencies (this optimizes Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the code
COPY . .

# 6. Grant execution permissions to the entrypoint script
RUN chmod +x entrypoint.sh

# 7. Run the script by default when the container starts
CMD ["./entrypoint.sh"]