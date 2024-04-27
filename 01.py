def numeros_impares (lista_numeros):
  lista_impares = []
  for numero in lista_numeros: # Verifica se o numero é impar verificando se o resto da divisão por 2 é diferente de 0
    if numero % 2 != 0:
      lista_impares.append(numero) # adiciona a lista de numeros impares
  return lista_impares

lista_numeros = [1,2,3,4,5,6,7,8,9,10,11]
lista_impares = numeros_impares(lista_numeros)
print(lista_impares)
