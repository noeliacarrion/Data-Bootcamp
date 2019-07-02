# bus.py



stops=[(10, 0), (4, 1), (3, 5), (3, 4), (5, 1), (1, 5), (5, 8), (4, 6), (2, 3)]



# numero de paradas
n_stops=len(stops)
print ('Numero de paradas: {}'.format(n_stops))


# numero de pasajeros en cada parada y ocupacion
occupation=[]
passengers=0
for i in range(len(stops)):
	passengers=passengers+stops[i][0]-stops[i][1]
	occupation.append(passengers)
print ('Ocupacion: {}'.format(occupation))



# maximo de ocupacion
max_occu=max(occupation)
print ('Maxima ocupacion: {}'.format(max_occu))




# media y desviacion estandar
media=sum(occupation)*1.0/len(occupation)        # media 
print ('Media: {:.4f}'.format(media))                       
std=0
for i in occupation:                
	std=std+(i-media)**2/(len(occupation)-1)     # std 
print ('Desviacion estandar: {:.4f}'.format(std**(0.5))) 



