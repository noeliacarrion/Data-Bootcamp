# plot_ji_dos.py


import sys
print(sys.version[:100])           # version del sistema (actual 3.7.2)
import numpy as np                 # numerical python, algebra lineal
from scipy.stats import chi2       # libreria estadistica de scipy, distribucion ji-dos
import matplotlib.pyplot as plt    # para plots



x=np.linspace(0,8,100)                       # espaciado lineal entre 0 y 8, 100 puntos, se discretiza el eje x
nus=[1,2,3,5]                                # parametro nu, grados de libertad
for nu in nus:                               # se dibuja para todos los nu
	y=chi2.pdf(x,nu)                         # ji-dos
	ax=plt.plot(x,y,label="$\\nu=%s$" % nu)  # se dibuja, con la leyenda
plt.xlabel("x")                              # etiqueta x
plt.ylabel("P(x)")                           # etiqueta y 
plt.legend(title="grados de libertad")       # titulo leyenda
plt.title("Distribucion   $\\chi2$")         # titulo 
plt.show()                                   # dibuja
