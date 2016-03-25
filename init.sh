#!/bin/bash
rm -rf /etc/nginx/nginx.conf
ln -s  /home/box/web/etc/nginx.conf /etc/nginx/nginx.conf
rm -rf /etc/nginx/sites-enabled/default
ln -s  /home/box/web/etc/hello.conf /etc/gunicorn.d/hello
/etc/init.d/nginx restart
/etc/init.d/gunicorn restart
