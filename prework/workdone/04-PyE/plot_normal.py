# plot_normal.py


import sys
print(sys.version[:100])           # version del sistema (actual 3.7.2)
import numpy as np                 # numerical python, algebra lineal
from scipy.stats import norm       # libreria estadistica de scipy, distribucion normal
import matplotlib.pyplot as plt    # para plots




x=np.linspace(-4,4,100)            # espaciado lineal entre -5 y 5, 100 puntos, se discretiza el eje x
mu=0                               # media
sigma=[0.5,1,2,3,4]                    # std
for s in sigma:                    # se dibuja para todos los lambda
	y=norm.pdf(x,mu,s)             # distribucion exponencial
	ax=plt.plot(x,y,label="$\\sigma=%s$" % s)  # se dibuja, con la leyenda 
plt.xlabel("x")                        # etiqueta x
plt.ylabel("P(x)")                     # etiqueta y
plt.legend(title="Parametros")         # titulo leyenda
plt.title("Distribucion Normal")  # titulo 
plt.show()                             # dibuja
