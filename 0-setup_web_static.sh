#!/usr/bin/env bash
#a Bash script that sets up your web servers for the deployment of web_static


# check if nginx is installed
if command -v nginx &> /dev/null; then
    echo "Nginx is already installed."
else
    echo "Nginx is not installed."
    echo "Installing process..."
    sudo apt-get -y update
    sudo apt-get  install -y nginx
fi
# make the required directory

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

#changing of ownership
sudo chown -R ubuntu:ubuntu /data/

#updating nginx configurations
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
# Restarting Nginx
sudo service nginx restart
exit 0
