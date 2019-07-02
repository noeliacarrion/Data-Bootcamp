# temperature.py

import numpy as np
import matplotlib.pyplot as plt


# axis x, axis y
y = [33,66,65,0,59,60,62,64,70,76,80,81,80,83,90,79,61,53,50,49,53,48,45,39]
x = list(range(len(y)))

# plot
plt.plot(x, y)
plt.axhline(y=70, linewidth=1, color='r')
plt.xlabel('hours')
plt.ylabel('Temperature ºC')
plt.title('Temperatures of our server throughout the day')
plt.show()



# Minimo
print ('Minimo de temperatura: %s' % min(y))
print ('')

# Maximo
print ('Maximo de temperatura: %s' % max(y))
print ('')


# elementos mayores de 70 grados
M_70=[]    # lista de elementos
n_70=0     # numero de elementos
for i in range(len(y)):
	if y[i]>70:
		M_70.append(y[i])
		n_70+=1
print ('Numero de elementos mayores que 70: %s' % n_70)
print (M_70)
print ('')



# media de temperatura a lo largo del dia
print ('Media de temperatura diaria: %s' % np.mean(y))
print ('')



# arreglando fallo del sensor
for i in range(len(y)):
	if y[i]==0:
		y[i]=(y[i-1]+y[i+1])/2
# plot
plt.plot(x, y)
plt.axhline(y=70, linewidth=1, color='r')
plt.xlabel('hours')
plt.ylabel('Temperature ºC')
plt.title('Temperatures of our server throughout the day (fixed)')
#plt.show()




# grados fahrenheit

def Fahrenheit(C):   # convierte grados celsius a fahrenheit
	F=(C*1.8)+32
	return F
	
y_F=[]    # lista de grados fahrenheit
for i in range(len(y)):
	f=Fahrenheit(y[i])
	y_F.append(f)
print ('Lista de temperaturas en ºF:')
print (y_F)
print ('')	





# toma de decisiones
# se cambia el funcionamiento del sistema de refrigeracion si pasan 4 horas con mas de 70ºC, 
# si la temperatura sube de 80ºC o si la media sube de 65ºC

# media movil
N=4        # media movil de 4 horas
suma=[0]
media_mov=[]
for i, j in enumerate(y,1):
	suma.append(suma[i-1]+j)
	if i>N:
		media_movil=(suma[i]-suma[i-N])/N
		media_mov.append(media_movil)
#print (media_mov)

for i in range(len(media_mov)):   # bucle para chequeo del sistema de refrigeracion
	if media_mov[i]>65:
		C=True
	elif y[i]>70 and y[i+1]>70 and y[i+2]>70 and y[i+3]>70:
		C=True
	elif y[i]>80 or y[i+1]>80 or y[i+2]>80 or y[i+3]>80:
		C=True	
	else:
		C=False	
	print (C)	
plt.show()
print ('')




# futuras mejoras

# horas donde T>70
horas=[]
for i in range(len(y)):
	if y[i]>70:
		horas.append(i)
print ('Horas donde T>70:', horas)
print ('')



# medias y std ºC y ºF
media_C=np.mean(y)
std_C=np.std(y)
print ('Media ºC: {:.2f}'.format(media_C))
print ('Std  ºC : {:.2f}'.format(std_C))
print ('')
media_F=np.mean(y_F)
std_F=np.std(y_F)
print ('Media ºF: {:.2f}'.format(media_F))
print ('Std  ºF : {:.2f}'.format(std_F))
print ('')
print ('Relacion (def F con la media ºC): {:.2f}'.format(Fahrenheit(media_C)))
print ('Relacion (def F con la std ºC-32): {:.2f}'.format(Fahrenheit(std_C)-32))
print ('')








