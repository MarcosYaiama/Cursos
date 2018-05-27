def MinMax(temperatura):
	print("A menor temperatura do mes foi: ", minima(temperatura), "C.")
	print("A maxima temperatura do mes foi: ", maxima(temperatura), "C.")

def maxima(temps):
	max = temps[0]
	i = 1
	while(i < len(temps)):
		if temps[i] > max:
			max = temps[i]
		i += 1
	return max



def minima(temps):
	min = temps[0]
	i = 1
	while(i < len(temps)):
		if temps[i] < min:
			min = temps[i]
		i += 1
	return min

def teste_pontual(temp, valor_esperado,teste):
	valor_calculado = teste(temp)
	if valor_calculado != valor_esperado:
		print("Valor errado para array", temp)
		print("Valor esperado: ",valor_esperado, ". Valor calculado: ", valor_calculado)

def testa_minima():
	print("Iniciando os testes")
	teste_pontual([0], 0,minima)
	teste_pontual([0,0,0,0,0,0], 0,minima)
	teste_pontual([0, 1, 2, 3,  4, 5, 6, 7, 8, 9, 10], 0, minima)
	teste_pontual([30,27,25,26,29,31,32,33,30,29,24,26,30,27,24,25,26,24,22, 23, 25, 25,28,28,32,32,31,29,28,31,33], 22, minima)	
	teste_pontual([-15,-12,-0,20,30], -15,minima)
	print("Finalizando os testes")


def testa_maxima():
	print("Iniciando os testes")
	teste_pontual([0], 0, maxima)
	teste_pontual([0,0,0,0,0,0], 0, maxima)
	teste_pontual([0, 1, 2, 3,  4, 5, 6, 7, 8, 9, 10], 10, maxima)
	teste_pontual([30,27,25,26,29,31,32,33,30,29,24,26,30,27,24,25,26,24,22, 23, 25, 25,28,28,32,32,31,29,28,31,33], 33, maxima)	
	teste_pontual([-15,-12,-0,20,30], 30,maxima)
	print("Finalizando os testes")
