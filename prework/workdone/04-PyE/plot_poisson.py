# plot_poisson.py

import sys
print(sys.version[:100])           # version del sistema (actual 3.7.2)
import numpy as np                 # numerical python, algebra lineal
from scipy.stats import poisson    # distribucion de Poisson
import matplotlib.pyplot as plt    # para plots
import math



x=[i for i in range(15)]           # 10 puntos, se discretiza el eje x
lambdas=[0.5,1,2,3,4,5,9]              # parametros lambda (media)
for lamb in lambdas:               # se dibuja para todos los lambda
	y=poisson.pmf(x,lamb)          # distribucion de Poisson   poison.pmf(x,lamb)=(lam**x)*exp(-lam)/factorial(x)     
	ax=plt.plot(x,y,label="$\\lambda=%s$" % lamb)  # se dibuja, con la leyenda 
plt.xlabel("x")                        # etiqueta x
plt.ylabel("P(x)")                     # etiqueta y
plt.legend(title="Parametros")         # titulo leyenda
plt.title("Distribucion Poisson")  # titulo 
plt.show()                             # dibuja
