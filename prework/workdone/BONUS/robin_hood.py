# robin_hood.py
import numpy as np
import matplotlib.pyplot as plt


# disparos
points=[(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5),
        (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
        (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2),
        (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]
#print (len(points))

for i in range(len(points)):    # plot de disparos y diana
	plt.plot(points[i][0], points[i][1], 'ro')
x=np.linspace(-11.0, 11.0, 100)   # para circunferencia diana
y=np.linspace(-11.0, 11.0, 100)
z, t=np.meshgrid(x,y)
F=(z)**2+(t)**2-9**2
plt.contour(z,t,F,[0])
plt.show()	




# ¿flecha sobre flecha?
'''
mejor con conjunto
len(points)==len(set(points))  # tienen que ser iguales si no hay repetidos
'''
arrow2=0
for i in range(len(points)):
	for j in range(len(points)):
		if points[i]==points[j] and i!=j:
			arrow2+=1
if arrow2>0:
	print ('I did it, I hit an arrow with another arrow.')			



# por cuadrantes
q1=0
q2=0
q3=0
q4=0
for i in range(len(points)):
	if points[i][0]>=0 and points[i][1]>0:
		q1+=1
	elif points[i][0]<0 and points[i][1]>0:
		q2+=1	
	elif points[i][0]<=0 and points[i][1]<0:
		q3+=1
	elif points[i][0]>0 and points[i][1]<0:
		q4+=1		
print ('Quadrants:  q1:%s, q2:%s, q3:%s, q4:%s' % (q1, q2, q3, q4))   # numero de flechas por cuadrantes




# punto mas cercano al centro de la diana
def ro(x, y):            # ro, distancia al origen de coordenadas
    r=np.sqrt(x**2+y**2)
    return r
    
d=[]        # lista de distancias
puntos_m=[] # puntos distancia minima
for i in range(len(points)):
	d.append(ro(points[i][0], points[i][1]))
for i in range(len(points)):		
	if ro(points[i][0], points[i][1])==min(d):
		puntos_m.append(points[i])		
print ('Closest points to the center: {}'.format(puntos_m))   # hay dos puntos a igual distancia




# ¿cuantas flechas hay que ir a buscar si ro=9? 
arrow_out=0
for i in range(len(points)):
	if ro(points[i][0], points[i][1])>9:
		arrow_out+=1
print ('Lost arrows:', arrow_out)		





