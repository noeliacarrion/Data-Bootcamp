# snail_and_well.py
import numpy as np

well_height=125             # 125 cm
daily_advance=30            # 30 cm 
night_retreat=20            # 20 cm

days=0       # dias

accumulated_distance=0                                       # distancia acumulada


while True:                                                  # mientras la distancia acumulada sea menor que la profundidad del pozo...
	accumulated_distance+=daily_advance                      # actualiza distancia acumulada
	days+=1                                                  # actualiza el numero de dias
	if accumulated_distance>=well_height:
		break
	else:
		accumulated_distance-=night_retreat	
	
print ('Days', days)
print ('')



# bonus

advance_cm=[30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]

days=0       # dias

accumulated_distance=0    # distancia acumulada


while True:                                                    # mientras la distancia acumulada sea menor que la profundidad del pozo...
	accumulated_distance+=advance_cm[days]                     # actualiza distancia acumulada
	days+=1	                                                   # actualiza el numero de dias
	if accumulated_distance>=well_height:
		break
	else:
		accumulated_distance-=night_retreat	
	
		

	
print ('Bonus')	
print ('Days', days)
daily_displacement=[]
for i in range(days):
	daily_displacement.append(advance_cm[i]-night_retreat)
print ('Max daily displacement', max(daily_displacement))	
print ('Min daily displacement', min(daily_displacement))	
print ('Average progress {:.4f}'.format(np.mean(daily_displacement)))
print ('Std progress {:.4f}'.format(np.std(daily_displacement)))









def snail(well_height, daily_advance, night_retreat):
	days=0       
	accumulated_distance=0                                       
	while True:                                                 
		accumulated_distance+=daily_advance                    
		days+=1                                                  
		if accumulated_distance>=well_height:
			break
		else:
			accumulated_distance-=night_retreat	
			
	return days	
	



# snail=lambda c,d,n:-(min(0,d-c)//(d-n))+1






print ("Basic Tests\n")

print (snail(3,2,1))      # 2
print (snail(10,3,1))     # 5
print (snail(10,3,2))     # 8
print (snail(100,20,5))   # 7
print (snail(5,10,3))     # 1










