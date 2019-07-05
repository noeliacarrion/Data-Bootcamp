# calc.py



import argparse



def suma(a,b):        # funcion suma
	return a+b



def resta(a,b):       # funcion resta
	return a-b

	

def multi(a,b):       # funcion multiplicacion
	return a*b
	
	
	
def divi(a,b):        # funcion division
	return a/b



	
def main():           # funcion principal
	
	parser=argparse.ArgumentParser()                 # analizador de argumentos
	 
	grupo=parser.add_mutually_exclusive_group()      # grupo mutuamente excluyente (solo una operacion)
	
	grupo.add_argument('-s', '--sum', help='Realiza la suma de dos numeros.', action='store_true')           # action guarda el argumento
	grupo.add_argument('-r', '--rest', help='Realiza la resta de dos numeros.', action='store_true')
	grupo.add_argument('-m', '--mult', help='Realiza la multiplicacion de dos numeros.', action='store_true')
	grupo.add_argument('-d', '--div', help='Realiza la division de dos numeros.', action='store_true')
	
	
	parser.add_argument('n1', help='Primer numero de la operacion.', type=float)
	parser.add_argument('n2', help='Segundo numero de la operacion.', type=float)	
	
	
	args=parser.parse_args()
	
	
	# opciones
	
	if args.sum: print ('El resultado de sumar {} con {} es {}'.format(args.n1, args.n2, (suma(args.n1, args.n2))))
	
	elif args.rest: print ('El resultado de resta {} con {} es {}'.format(args.n1, args.n2, (resta(args.n1, args.n2))))
	
	elif args.mult: print ('El resultado de multiplicar {} con {} es {}'.format(args.n1, args.n2, (multi(args.n1, args.n2))))
	
	elif args.div: print ('El resultado de dividir {} con {} es {}'.format(args.n1, args.n2, (divi(args.n1, args.n2))))
	
	else: print ('Error: se requiere un argumento para realizar la accion.')
	
	
if __name__=='__main__':
	main()
	
	
	
	
	
	
	
	
	
	
	
	

