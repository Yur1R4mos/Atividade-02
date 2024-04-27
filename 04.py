def segundo_maior_valor(lista_numeros):
  lista_ordenada = sorted(set(lista_numeros), reverse=True) # Ordena a lista do maior para o menor
  if len(lista_ordenada) >= 2: # Verifica se tem pelo menos dois numeros na lista se tiver retorna o indice [1] que é o segundo da lista
    return lista_ordenada[1]  
  else:
    return None  

lista_numeros = [1,2,4,6,8,3]
segundo_maior = segundo_maior_valor(lista_numeros)
print(segundo_maior)
