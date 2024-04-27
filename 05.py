def ordem_alfabetica (lista_pessoas):
  return sorted(lista_pessoas, key = lambda pessoa: pessoa[0]) # Ordena a lista de tuplas pelo indice [0] (nome da pessoa)

lista_pessoas = [("Yuri", 21),("Maria", 82),("Yara", 24),("Carlos", 23)]
lista_ordenada = ordem_alfabetica(lista_pessoas)
print(lista_ordenada)
