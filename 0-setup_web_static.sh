#!/usr/bin/env bash
"""
a Bash script that sets up your web servers for the deployment of web_static
"""


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
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

#creating a fake html file
echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html

# creating a symbolic link
ln -s /data/web_static/releases/test/ /data/web_static/current

#changing of ownership
sudo chown -R ubuntu:ubuntu /data/

#updating nginx configurations
sudo sed -i 's|^.*server_name.*$|&\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n|' /etc/nginx/sites-available/default

# Restarting Nginx
sudo service nginx restart

exit 0
