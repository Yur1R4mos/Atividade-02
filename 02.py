def verifica_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1): # Verifica se o número é primo iterando de 2 até a raiz quadrada do numero + 1        
        if numero % i == 0:                    # pois se um numero não é primo ele pode ser divido em duas partes que estara no intervalo de 2 a raiz do numero
            return False         
    return True

def listar_primos (lista_numeros):
    primos = []
    for numero in lista_numeros:
        if verifica_primo(numero):
            primos.append(numero)
    return primos

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primos = listar_primos(lista_numeros)
print(primos)
