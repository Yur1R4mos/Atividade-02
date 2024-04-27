def listar_numeros_unicos (lista1, lista2):
  numeros_unicos_total = []
  for numero in lista1: # Verifica os numeros unicos na primeira lista e adiciona a lista de numeros unicos
    if numero not in lista2:
      numeros_unicos_total.append(numero)
      
  for numero in lista2: # Verifica os numeros unicos na segunda lista e adiciona a lista de numeros unicos
    if numero not in lista1:
      numeros_unicos_total.append(numero)
      
  return numeros_unicos_total

lista1 = [1,2,3,4,5]
lista2 = [2,3,5,6,7,8]
numeros_unicos = listar_numeros_unicos(lista1, lista2)
print(numeros_unicos)
