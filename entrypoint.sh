#!/bin/bash
python3 /root/GetAzureServiceTags.py
systemctl start cron
/usr/sbin/apache2ctl -D FOREGROUND