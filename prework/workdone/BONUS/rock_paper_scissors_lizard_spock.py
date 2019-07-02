# rock_paper_scissors_lizard_spock.py

import random

print ('Game stone, paper, scissors, lizard, spock')
print ('')

hand=['stone', 'paper', 'scissors', 'lizard', 'spock']   # opciones del juego



g_max=3                   # numero de partidas     (games max) 
g_to_win=(g_max+1)/2      # al mejor de g_max      (games to win)



def cpu(hand):       # funcion para cpu
	return random.choice(hand)



def player(hand):   # funcion para jugador
	player=None
	print ('')
	print ('You have to choose; stone, paper, scissors, lizard or spock? :')
	while player not in hand:
		try:
			print ('')
			print ('Please, write correctly...')  # si te equivocas al escribir sigue el bucle
			player=str(input())
		except :
			player=None	
	return player


def game(cpu, player):   # funcion para juego
	if cpu==player:
		return 0      # empate
		
		
	if cpu=='stone' and player=='scissors':
		return 1       
	elif cpu=='stone' and player=='lizard':
		return 1 	
	elif cpu=='paper' and player=='stone':
		return 1       
	elif cpu=='paper' and player=='spock':
		return 1 	
	elif cpu=='scissors' and player=='paper':
		return 1             
	elif cpu=='scissors' and player=='lizard':
		return 1       
	elif cpu=='lizard' and player=='paper':
		return 1
	elif cpu=='lizard' and player=='spock':
		return 1
	elif cpu=='spock' and player=='stone':
		return 1
	elif cpu=='spock' and player=='scissors':
		return 1		# gana cpu	
		
		
	if player=='stone' and cpu=='scissors':
		return 2       
	elif player=='stone' and cpu=='lizard':
		return 2 	
	elif player=='paper' and cpu=='stone':
		return 2       
	elif player=='paper' and cpu=='spock':
		return 2 	
	elif player=='scissors' and cpu=='paper':
		return 2             
	elif player=='scissors' and cpu=='lizard':
		return 2       
	elif player=='lizard' and cpu=='paper':
		return 2
	elif player=='lizard' and cpu=='spock':
		return 2
	elif player=='spock' and cpu=='stone':
		return 2
	elif player=='spock' and cpu=='scissors':
		return 2		# gana jugador			





def results(cpu, player, game, cpu_wins, player_wins, ties):  # funcion de resultados
	print ('')
	print ('CPU:', cpu)
	print ('Player:', player)
	if game==0:
		print ('Tie')
	elif game==1:
		print ('CPU Wins')
	elif game==2:
		print ('Player Wins')
	print ('Ties:', ties)	
	print ('Total wins CPU:', cpu_wins)	
	print ('Total wins Player:', player_wins)			
	


cpu_wins=0
player_wins=0
tie=0
while tie<=g_max:
	c=cpu(hand)
	p=player(hand)
	g=game(c,p)
	
	if g==0:
		tie+=1
	elif g==1:
		cpu_wins+=1
	elif g==2:
		player_wins+=1	
		
	r=results(c, p, g, cpu_wins, player_wins, tie)	
	
	if cpu_wins==g_to_win:
		print ('')
		print ('')
		print ('CPU Wins the Game')
		break 
	elif player_wins==g_to_win:
		print ('')
		print('')
		print ('Player Wins the Game')
		break 	
	elif tie==g_max:
		print ('')
		print ('')
		print ('Tie')		
		break














