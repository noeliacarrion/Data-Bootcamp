# plot_exponencial.py

import sys
print(sys.version[:100])           # version del sistema (actual 3.7.2)
import numpy as np                 # numerical python, algebra lineal
import matplotlib.pyplot as plt    # para plots



x=np.linspace(0,5,100)           # espaciado lineal entre 0 y 5, 100 puntos, se discretiza el eje x
lambdas=[0.5,1,2,3,4]            # parametros lambda
for lam in lambdas:                # se dibuja para todos los lambda
	y=lam*np.exp(-lam*x)           # distribucion exponencial
	ax=plt.plot(x,y,label="$\\lambda=%s$" % lam)  # se dibuja, con la leyenda 
plt.xlabel("x")                        # etiqueta x
plt.ylabel("P(x)")                     # etiqueta y
plt.legend(title="Parametros")         # titulo leyenda
plt.title("Distribucion Exponencial")  # titulo 
plt.show()                             # dibuja
