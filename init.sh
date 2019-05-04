sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/nginx.conf
sudo systemctl restart nginx 
sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo systemctl restart gunicorn
sudo systemctl start mysql
