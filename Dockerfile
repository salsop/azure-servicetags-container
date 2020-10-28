from ubuntu:latest

# Set Timezone
ENV TZ=Europe/London
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Upgrade and install base components
RUN apt update
RUN apt upgrade -y
RUN apt install -y systemctl
RUN apt install -y apache2
RUN apt install -y python3
RUN apt install -y python3-pip
RUN pip3 install requests
RUN apt install -y cron

# Setup Python Script
WORKDIR /root
COPY GetAzureServiceTags.py GetAzureServiceTags.py
RUN chmod +x GetAzureServiceTags.py

# Configure Cron
COPY ScheduledScriptExecution /root/ScheduledScriptExecution
RUN cat /root/ScheduledScriptExecution | crontab
RUN systemctl enable cron

# Container Entrypoint
COPY entrypoint.sh /root/entrypoint.sh
RUN chmod +x /root/entrypoint.sh
ENTRYPOINT /root/entrypoint.sh

# Exporse TCP/80
EXPOSE 80
