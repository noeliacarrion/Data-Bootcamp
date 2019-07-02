# plot_beta.py


import sys
print(sys.version[:100])           # version del sistema (actual 3.7.2)
import numpy as np                 # numerical python, algebra lineal
from scipy.stats import beta       # libreria estadistica de scipy, distribucion beta
import matplotlib.pyplot as plt    # para plots




x=np.linspace(0,1,100)                                  # espaciado lineal entre 0 y 1, 100 puntos, se discretiza el eje x
parametros=[(0.5, 0.5),(1, 1),(4, 3),(2, 5),(6, 6)]     # parametros alfa y beta
for p in parametros:                                    # se dibujan para todos los parametros
	y = beta.pdf(x, p[0], p[1])                         # (Beta(x,a,b))
	plt.plot(x,y,label="$\\alpha=%s$, $\\beta=%s$" %p)  # se dibuja, con la leyenda
plt.xlabel("$\\theta$")         # etiqueta x
plt.ylabel("Densidad")          # etiqueta y
plt.legend(title="Parametros")  # titulo leyenda
plt.title("Distribucion Beta")  # titulo
plt.show()                      # dibuja
