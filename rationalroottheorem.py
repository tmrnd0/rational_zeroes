#Este programita surgió de la necesidad de agilizar la evaluación de los posibles ceros de polinomios obtenidos usando el Teorema de Raices Racionales. En lugar de calcular cada posible raiz a digitación, se ingresa el polinomio y este devuelve las posibles raices, pero tambien evalua cada una de ellas localizando todos los ceros. Al evaluar para todas las posibles raices se puede obtener un analisis de la tendencia de la funcion y obtener una gráfica aproximada sin tener que hacer tablas. Mil disculpas por el Spanglish.

import sympy
from fractions import Fraction

print("\nCEROS DE POLINOMIOS SEGÚN EL TEOREMA DE RAICES RACIONALES\n")

while True:
	
	degree = input("Ingresá el grado del polinomio: ")
	
	try:
	
		if int(degree) > 1:
		
			try: 
				
				coefficients = []

				for number in range(0,int(degree)+1):
					
					coefficients.append(int(number))
					
				values_coefficients = []
				
				for coefficient in coefficients:
					
					asubn = input("\nIngresá el coeficiente entero a" + str(coefficient)+ "	")
					values_coefficients.append(asubn)
					
				p = int(values_coefficients[int(degree)])			
				q = int(values_coefficients[0])

				#Building the function:

				function = []
				Function = []

				x = sympy.symbols("x")
				

				for anumber in range(0,int(degree)+1):
					
					A = int(values_coefficients[anumber])
					Exp = (int(degree)-anumber)
					term = str(A) + str(x) + "^" + str(Exp)
					Term = A*x**Exp
					
					function.append(term)
					Function.append(Term)
					
				print("\nf(x) = " + " + ".join(map(str,function)))

				polinomio = sum(Function)
				
				#Calculating factors of leading and independent coefficients using libff; had to add some additional input since libff didn't give output for factors 0, 1, 2, 3:
		 
				print("\nFactores de p: \n")
				
				P = []
				
				if p == 0:
					print("-Cero no tiene factores-")	
					
				else:
					
					for i in range(1, abs(p) + 1):
						if abs(p) % i == 0:
							P.append(i)
					print(P)


				print("\nFactores de q: \n")

				Q = []
					
				if q == 0:
					print("-Cero no tiene factores- \n")	
					
				else:
					
					for i in range(1, abs(q) + 1):
						if abs(q) % i == 0:
							Q.append(i)
				
					print(Q)

				values = []
				
				#Evaluating the Rational Roots Theorem p/q:

				for factor_p in P:
					for factor_q in Q:
						
						poss_root = int(factor_p)/int(factor_q)
						values.append(poss_root)
								
						poss_root = -int(factor_p)/int(factor_q)
						values.append(poss_root)

				print("\nPosibles raices del polinomio (p/q): \n")

				if len(values) == 0:
					
					print("...Para obtener las raices, resolver para x si y = 0.\n")

				else:	
					print(values)
				
					#Evaluating the polynomial for each rational root possibility:

					roots = []

					print("\nEvaluando el polinomio para cada posible raiz: ")

					for value in values:
						
						f = polinomio.subs(x, value)
						
						if f == 0:
							roots.append(value)
					
						print("\nF(" +str(value)+ ")" + " = " + str(f))
						
					#Results:	
						
					if len(roots) == 0:
						print("\n-El polinomio no tiene raices reales o raices reales racionales-\n")

					else:
						print("\nLas raices reales racionales del polinomio son: \n")
						print("X = " + str(roots) + "\n")

			#Any error :P
			
			except:
							
				print("\nAlgo malo pasó, intentá de nuevo!\n")
		
		else:
			print("\nEl grado del polinomio debe ser mayor que 1. Para rectas simplemente evaluar y = 0.\n")
	except:
			
		print("El grado debe ser un número entero positivo\n")
