#!/bin/bash
rm -rf /etc/nginx/nginx.conf
ln -s  /home/box/web/etc/nginx.conf /etc/nginx/nginx.conf
rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
