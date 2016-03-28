#!/bin/bash
rm -rf /etc/nginx/nginx.conf
ln -sf  /home/box/web/etc/nginx.conf /etc/nginx/nginx.conf
rm -rf /etc/nginx/sites-enabled/default
ln -sf  /home/box/web/etc/hello.conf /etc/gunicorn.d/hello
ln -sf  /home/box/web/etc/ask.conf /etc/gunicorn.d/ask
/etc/init.d/nginx restart
/etc/init.d/gunicorn restart
