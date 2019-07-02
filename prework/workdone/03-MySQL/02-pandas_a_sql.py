# -*- coding: utf-8 -*-
# pandas_to_mysql.py  



import sys
print(sys.version[:100])               # version del sistema (actual 3.7.2)
from sqlalchemy import create_engine   # conexion mysql      
import pandas as pd                    # dataframe




datos=pd.read_csv('apple_store.csv')              # se leen los datos del archivo csv
print ('Datos leidos.')
#print (datos)

motor=create_engine('mysql+mysqlconnector://admin:password@localhost:3306/Apps')   # motor de enlace

datos.to_sql(name='Ratings', con=motor, if_exists='append', index=False)           # datos a sql
print ('Datos copiados a SQL.')


