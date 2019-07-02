# -*- coding: utf-8 -*-
# mtcars.py  


import sys
print(sys.version[:100])              # version del sistema (actual 3.7.2)
import pandas as pd                   # dataframe
import numpy as np                    # numerical python, algebra lineal
from scipy import stats               # libreria estadistica de scipy
import random as rnd                  # para muestreo aleatorio
from matplotlib import pyplot as plt  # para plots
import seaborn as sns                 # para plots



print ("DATOS")
datos=pd.read_csv('mtcars.csv')  # se leen los datos del archivo csv, si el archivo csv esta en la misma carpeta que el archivo py no es necesario escribir la ruta, en caso contrario reescribir esta linea
print (datos)
print ("_________________________________")
print ("_________________________________")

print ("MEDIDAS DE TENDENCIA CENTRAL")
print ("_________________________________")
media_mpg=np.mean(datos['MPG'])              # media MPG (millas por galon)
print ('')
print ("Media MPG      : %f " % media_mpg)
print ("_________________________________")
mediana_mpg=np.median(datos['MPG'])          # mediana MPG 
print ('')
print ("Mediana MPG    : %s " % mediana_mpg)
print ("_________________________________")
moda_mpg=stats.mode(datos['MPG'])            # moda MPG (con scipy, multimodal, da la moda mas baja (10.4, 15.2, 19.2, 21, 21.4, 22.8, 30.4), multiplicidad 2)
print ('') 
print ("Moda MPG       : %s " % moda_mpg[0][0])
print ("_________________________________")

print ("MEDIDAS DE DISPERSION")
print ("_________________________________")
min_mpg=np.min(datos['MPG'])                 # minimo MPG 
print ('') 
print ("Minimo MPG     : %s " % min_mpg)
print ("_________________________________")
max_mpg=np.max(datos['MPG'])                 # maximo MPG 
print ('') 
print ("Maximo MPG     : %s " % max_mpg)
print ("_________________________________")
rango_mpg=max_mpg-min_mpg                    # rango MPG (rango dinamico) 
print ('')   
print ("Rango MPG      : %s " % rango_mpg)
print ("_________________________________")
p25_mpg=np.percentile(datos['MPG'],25)            # 25º percentil MPG 
print ('') 
print ("25º percentil MPG : %s " % p25_mpg)
print ("_________________________________")
p50_mpg=np.percentile(datos['MPG'],50)            # 50º percentil MPG 
print ('') 
print ("50º percentil MPG : %s " % p50_mpg)
print ("_________________________________")
p75_mpg=np.percentile(datos['MPG'],75)            # 75º percentil MPG 
print ('') 
print ("75º percentil MPG : %s " % p75_mpg)
print ("_________________________________")
rango_inter_mpg=p75_mpg-p25_mpg                    # rango intercuartil
print ('')
print ("Rango Intercuartil: %s" % rango_inter_mpg)
print ("_________________________________")

print ("MEDIDAS DE VARIABILIDAD")
print ("_________________________________")
var_mpg=np.var(datos['MPG'])                       # varianza MPG 
print ('') 
print ("Varianza MPG      : %f " % var_mpg)
print ("_________________________________")
std_mpg=np.std(datos['MPG'])                       # desviacion estandar MPG 
print ('') 
print ("Desvest MPG       : %f " % std_mpg)
print ("_________________________________")
mad_mpg=datos['MPG'].mad()                         # mad, desviacion media absoluta MPG 
print ('') 
print ("Desv. media abs.  : %f " % mad_mpg)
print ("_________________________________")
print ("_________________________________")

frec_mpg=np.unique(datos['MPG'],return_counts=True)   # frecuencias de cada numero
print ('') 
print ("FRECUENCIAS")

for i in range(len(frec_mpg[0])):
	print ('') 
	print ("Nº:",frec_mpg[0][i],"--- frecuencia:",frec_mpg[1][i])  # numero y su frecuencia
	print ("_________________________________")
	# falta la frecuencia segun intervalo
plt.figure(1)
plt.hist(datos[['MPG']].values, range(10,40,5))       # histograma, con ese rango sale por intervalos
plt.xlabel("MPG")        # etiqueta x
plt.ylabel("nº")         # etiqueta y 
plt.title("MPG")         # titulo 
#plt.show()               # dibuja


print ("_________________________________")
print ("_________________________________")

print ("MUESTREO")
print ("_________________________________")
           
datos_array=[]      # se ponen los datos en una lista para el random
for l in range(len(datos)):
	datos_array.append(datos['MPG'][l])
j=0
k=20       # numero de muestras
while j<k:
	muestra=rnd.sample(datos_array,15)  # muestreo aleatorio, 15 elementos por muestra, k muestras
	med=np.mean(muestra)                # media de la muestra
	print ("Muestra : %s   Media : %f" % (j+1,med))
	print ("_________________________________")
	j+=1



print ("_________________________________")
print ("_________________________________")

print ("CORRELACION - r2")
print ("_________________________________")
corr_mpg_dsp=np.corrcoef(datos['MPG'],datos['Displacement'])            # coeficiente de correlacion Pearson, MPG-Displacement (millas por galon-cilindrada(pulgadas cubicas)) 
print ('') 
print ("Correlacion MPG-DSP  : %f " % corr_mpg_dsp[0][1])               # np.corrcoef devuelve la matriz 2x2
print ("_________________________________")
corr_dsp_hp=np.corrcoef(datos['Displacement'], datos['Horsepower'])     # coeficiente de correlacion Pearson, Displacement-Horsepower (cilindrada-potencia)
print ('') 
print ("Correlacion DSP-HP   : %f " % corr_dsp_hp[0][1])
print ("_________________________________")  
print ("_________________________________")  
print ('') 
print ("DETERMINACION - R2")                                            # en el caso de regresion lineal R2=r**2
print ("_________________________________") 
print ('') 
print ("R2 MPG-DSP  : %f " % corr_mpg_dsp[0][1]**2)               
print ("_________________________________")
print ('') 
print ("R2 DSP-HP   : %f " % corr_dsp_hp[0][1]**2)
print ("_________________________________")  
print ("_________________________________")  
print ('') 
print ("Matriz Correlacion   :")                              # matriz de correlacion con pandas
print (datos.corr())
plt.figure(2)
#plt.matshow(datos.corr())                                    # plot de la matriz de correlacion
sns.heatmap(datos.corr())
plt.title("Correlacion")                                      # titulo 
#plt.show()                                                    # dibuja
print ("_________________________________")
print ("_________________________________")
print ("_________________________________")

print ("REGRESION  y=m*x+b  Displacement vs MPG")
print ("_________________________________")

plt.figure(3)
plt.scatter(datos['MPG'],datos['Displacement'])               # plot de puntos Displacement vs MPG
plt.xlabel("MPG")                                             # etiqueta x
plt.ylabel("Displacement")                                    # etiqueta y 
plt.title("Displacement vs MPG")                              # titulo 
#plt.show()                                                    # dibuja

est_lineal=np.polyfit(datos['MPG'],datos['Displacement'],1)   # ajuste lineal con numpy (x,y,grado del ajuste)
m1=est_lineal[0]    # pendiente m
b1=est_lineal[1]    # ordenada en el origen b
print ("_________________________________")
print ("Pendiente m1 : %s" % m1)
print ("_________________________________")
print ("Ordenada en el origen b1 : %.2f" % b1)
print ("_________________________________")

plt.figure(4)
plt.scatter(datos['MPG'],datos['Displacement'])               # plot de puntos Displacement vs MPG 
plt.plot(datos['MPG'],m1*datos['MPG']+b1, color = 'r')        # recta de ajuste
plt.text(25,400,"Disp=%.2fMPG+%.2f" % (m1,b1))                # texto en plot (x,y,texto), ecuacion de la recta
plt.xlabel("MPG (x)")                                         # etiqueta x
plt.ylabel("Displacement (y)")                                # etiqueta y 
plt.title("Displacement vs MPG")                              # titulo 
#plt.show()                                                    # dibuja

print ("_________________________________")
print ("_________________________________")
print ("REGRESION  y=m*x+b  MPG vs Displacement")
print ("_________________________________")

est_lineal2=np.polyfit(datos['Displacement'],datos['MPG'],1)   # ajuste lineal con numpy (x,y,grado del ajuste)
m2=est_lineal2[0]    # pendiente m
b2=est_lineal2[1]    # ordenada en el origen b
print ("_________________________________")
print ("Pendiente m2 : %s" % m2)
print ("_________________________________")
print ("Ordenada en el origen b2 : %.2f" % b2)
print ("_________________________________")

plt.figure(5)
plt.scatter(datos['Displacement'],datos['MPG'])                                 # plot de puntos  MPG vs Displacement
plt.plot(datos['Displacement'],m2*datos['Displacement']+b2, color = 'r')        # recta de ajuste
plt.text(300,30,"MPG=%.3fDisp+%.2f" % (m2,b2))                                  # texto en plot (x,y,texto), ecuacion de la recta
plt.xlabel("Displacement (x)")                                                  # etiqueta x
plt.ylabel("MPG (y)")                                                           # etiqueta y 
plt.title("MPG vs Displacement")                                                # titulo 
plt.show()                                                                      # dibuja



'''
print ("_________________________________")
print ("_________________________________")
print ("REGRESION  y=a2*x**2+a1*x+a0")
print ("_________________________________")
est_cuadratica=np.polyfit(datos['MPG'],datos['Displacement'],2)   # ajuste cuadratico (x,y,grado del ajuste)
a2=est_cuadratica[0]    # factor cuadratico
a1=est_cuadratica[1]    # factor lineal
a0=est_cuadratica[2]    # ordenada en el origen 
print ("_________________________________")
print (" Factor cuadratico: %.2f" % a2)
print ("_________________________________")
print (" Factor lineal    : %.2f" % a1)
print ("_________________________________")
print ("Ordenada en el origen b : %.2f" % a0)
print ("_________________________________")

plt.figure(5)
plt.scatter(datos['MPG'],datos['Displacement'])                                    # plot de puntos Displacement vs MPG 
plt.plot(datos['MPG'],(a2*(datos['MPG']**2))+(a1*datos['MPG'])+a0, color = 'r')    # curva de ajuste
plt.xlabel("MPG")                                                                  # etiqueta x
plt.ylabel("Displacement")                                                         # etiqueta y 
plt.title("Displacement vs MPG")                                                   # titulo 
plt.show()                                                                         # dibuja
'''

'''
print ("_________________________________")
print ("_________________________________")
print ("REGRESION  y=a3*x**3+a2*x**2+a1*x+a0")
print ("_________________________________")
est_cubica=np.polyfit(datos['MPG'],datos['Displacement'],3)   # ajuste cubico (x,y,grado del ajuste)
a3=est_cubica[0]    # factor cubico 
a2=est_cubica[1]    # factor cuadratico 
a1=est_cubica[2]    # factor lineal 
a0=est_cubica[3]    # ordenada en el origen b
print ("_________________________________")
print (" Factor cubico    : %.2f" % a3)
print ("_________________________________")
print (" Factor cuadratico: %.2f" % a2)
print ("_________________________________")
print (" Factor lineal    : %.2f" % a1)
print ("_________________________________")
print ("Ordenada en el origen b : %.2f" % a0)
print ("_________________________________")

plt.figure(6)
plt.scatter(datos['MPG'],datos['Displacement'])                                                           # plot de puntos Displacement vs MPG 
plt.plot(datos['MPG'],a3*(datos['MPG']**3)+a2*(datos['MPG']**2)+a1*datos['MPG']+a0, color = 'r')          # curva de ajuste
plt.xlabel("MPG")                                                                  # etiqueta x
plt.ylabel("Displacement")                                                         # etiqueta y 
plt.title("Displacement vs MPG")                                                   # titulo 
plt.show()                                                                         # dibuja
'''
