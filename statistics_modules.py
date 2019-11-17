import statistics

def arr_int(arr):
  return [int(n) for n in arr]

def mediana(arr):
  arr = arr_int(arr)
  if(len(arr) < 11):
    return statistics.median(arr)
  return None

def amplitude(arr):
  arr = arr_int(arr)
  if(len(arr) < 11):
    return max(arr) - min(arr) 
  return None

def variancia(arr):
  arr = arr_int(arr)
  if(len(arr) < 11):
    return statistics.variance(arr)  
  return None

def getN1(n):	
	n1 = float(n)
	if n1 >= 0 and n1 <= 10:
		return n1
	else:
		return -1

def getN2(n):
	n2 = n			
	if n2 >= 0 and n2 <= 10:
		return n2
	else:
	 return	-1

def getN3(n):
	n3 = n			
	if n3 >= 0 and n3 <= 10:
		return n3
	else:
	 return	-1

def mediaPonderada(n1,n2,n3):
	nota1 = getN1(int(n1))
	nota2 = getN2(int(n2))
	nota3 = getN3(int(n3))

	if nota1 != -1 and nota2 != -1 and nota3 != -1:
		media = ((nota1 * 0.20) + (nota2 * 0.30) + (nota3 * 0.50)) / 3
		return media
	else:
		return None


def inserirNotas():
	listN = []
	if len(listN) == 0:
		listN.append(float(input('Insira a Primeira nota:')))			
		while len(listN) < 5:
			valor = float(input('Insira a próxima nota ou digite 102 para ver o resultado:'))
			if valor == 102:
				return listN 
			else:
				listN.append((valor))
	return listN



def media(arr):
	listNotas = arr_int(arr)
	if len(listNotas) > -1 and len(listNotas) <= 100:
		soma  = sum(listNotas) 
		qtdNotas = len(listNotas)
		return soma / qtdNotas
	else:
		return 0	

