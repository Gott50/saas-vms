#!/bin/bash
echo START Parameters: $@

sudo docker run -d -p 80:80 -p 5900:5900 -e RESOLUTION=$1x$2 -v /dev/shm:/dev/shm dorowu/ubuntu-desktop-lxde-vnc

echo Start shutdown.sh
nohup sudo bash ./vm_scripts/shutdown.sh