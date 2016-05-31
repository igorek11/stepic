pip install pymysql

#И в settings.py  прописал:

#import pymysql


pymysql.install_as_MySQLdb() 
mysql -uroot -e "CREATE DATABASE web;"
mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY '1234';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON web.* TO 'box'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
