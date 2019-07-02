# -*- coding: utf-8 -*-
# csv_a_mysql.py  



import sys
print(sys.version[:100])   # version del sistema (actual 3.7.2)
import MySQLdb as mdb      # base de datos, conexion mysql



db_host='localhost'         #host
db_user='admin'             #usuario
db_pass='password'          #password
db_name='Apps'              #nombre de la base de datos
con=mdb.connect(host=db_host, user=db_user, passwd=db_pass, db=db_name, autocommit=True, use_unicode=True, charset="utf8") #conecta con la base de datos
print ('Conectado.')
cur=con.cursor()            # cursor sql, para ejecutar comandos 


tabla ="""DROP TABLE IF EXISTS Ratings; 
          CREATE TABLE Ratings (
          id int,                        
          track_name varchar(255),    
          size_bytes bigint, 
          price float, 
          rating_count_tot float, 
          rating_count_ver float, 
          user_rating float, 
          user_rating_ver float, 
          prime_genre varchar(50))""" # se crea la tabla
          
          
cur.execute(tabla)
print ('Tabla creada.')


