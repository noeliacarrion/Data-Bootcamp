# plot_t_student.py


import sys
print(sys.version[:100])           # version del sistema (actual 3.7.2)
import numpy as np                 # numerical python, algebra lineal
from scipy.stats import t          # libreria estadistica de scipy, distribucion t de Student
import matplotlib.pyplot as plt    # para plots



x=np.linspace(-5,5,100)      # espaciado lineal entre -5 y 5, 100 puntos, se discretiza el eje x
nus=[1,2,5,50]               # parametro nu
for nu in nus:                     # se dibuja para todos los nu
	y=t.pdf(x,nu)                  # t(x,nu)
	ax=plt.plot(x,y,label="$\\nu=%s$" % nu)  # se dibuja, con la leyenda
plt.xlabel("x")                      # etiqueta x
plt.ylabel("P(x)")                   # etiqueta y 
plt.legend(title="Parametros")       # titulo leyenda
plt.title("Distribucion t-Student")  # titulo 
plt.show()                           # dibuja
