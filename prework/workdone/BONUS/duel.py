#duel.py



gandalf=[10, 11, 13, 30, 22, 11, 10, 33, 22, 22]     # conjuros de Gandalf
saruman=[23, 66, 12, 43, 12, 10, 44, 23, 12, 17]     # conjuros Saruman



Gandalf_wins=0    # victorias de Gandalf
Saruman_wins=0    # victorias de Saruman
Tie=0             # empate



for i in range(len(gandalf)):     # bucle en la longitud de los conjuros
	
	if gandalf[i]>saruman[i]:     # gana Gandalf
		Gandalf_wins+=1
		
	elif saruman[i]>gandalf[i]:   # gana Saruman
		Saruman_wins+=1
		
	else:                         # empate
		Tie+=1		



# Imprime quien gana
print ('Round 1')
if Gandalf_wins>Saruman_wins and Gandalf_wins>Tie:
	print ('Gandalf Wins')

if Saruman_wins>Gandalf_wins and Saruman_wins>Tie:
	print ('Saruman Wins')

if Tie>Saruman_wins and Tie>Gandalf_wins:
	print ('Tie')






# Bonus (Round2)

POWER={'Fireball': 50, 'Lightning bolt': 40, 'Magic arrow': 10, 'Black Tentacles': 25, 'Contagion': 45}
spell=[]
for string, valor in POWER.items():  # se convierte el diccionario en una lista para bucle
	k=[string, valor]
	spell.append(k)
	
#print (spell)
 	
gandalf=['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball', 'Magic arrow', 'Lightning bolt', 'Fireball', 'Fireball', 'Fireball']
saruman=['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles', 'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']



for i in range(len(gandalf)):          # bucle comparando strings y reasignando valores
	for j in range(len(spell)):
		if gandalf[i]==spell[j][0]:
			gandalf[i]=spell[j][1]
		if saruman[i]==spell[j][0]:
			saruman[i]=spell[j][1]	

#print (gandalf)
#print (saruman)
print ('')
print ('')
print ('Round 2')
for i in range(len(gandalf)-2):
	if gandalf[i]>saruman[i] and gandalf[i+1]>saruman[i+1] and gandalf[i+2]>saruman[i+2]:
		print ('Gandalf Wins')
		break
	if gandalf[i]<saruman[i] and gandalf[i+1]<saruman[i+1] and gandalf[i+2]<saruman[i+2]:
		print ('Saruman Wins')	
		break
 
 
print ('') 
print ('') 
media_g=sum(gandalf)*1.0/len(gandalf)            # media Gandalf
print ('Mean Gandalf: ', media_g)                        
std_g=0
for i in gandalf:                
	std_g=std_g+(i-media_g)**2/(len(gandalf)-1)  # std Gandalf
print ('Std Gandalf: {:.3f}'.format(std_g**(0.5)))          
print ('') 
media_s=sum(saruman)*1.0/len(saruman)            # media Saruman
print ('Mean Saruman: ', media_s)                       
std_s=0
for i in saruman:                
	std_s=std_s+(i-media_s)**2/(len(saruman)-1)  # std Saruman
print ('Std Saruman: {:.3f}'.format(std_s**(0.5)))
         






