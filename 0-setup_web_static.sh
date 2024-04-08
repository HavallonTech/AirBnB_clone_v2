#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx
mkdir -p data/web_static/releases/test
mkdir -p data/web_static/shared
echo "<html>
	<head>
	<title>
	<body>
    	Holberton School
  	</body>
	</html>" > /data/web_static/current/index.html
#create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current
#change ownership
chown -R ubuntu:ubutu  /data/
#update Nginx server configuration
sudo sed -i 's|^.*server_name.*$|&\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n|' /etc/nginx/sites-available/default


# Restart Nginx
sudo service nginx restart
