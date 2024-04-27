#Supondo que já foi feita a importação da biblioteca pandas, primeiro instancia o arquivo pelo nome ou caminho completo do mesmo, depois usa a função pd.read_csv(nome_arquivo)
#para ler o arquivo e em seguida usa o print(df.head()) para exibir as primeiras linhas do csv 
import pandas as pd 
nome_arquivo = "exemplo.csv" # instacia uma variavel para guardar o nome ou caminho completo do arquivo.csv 
df = pd.read_csv(nome_arquivo) # Lê o arquivo csv especificado pelo nome ou caminho completo do arquivo e carrega os dados em um dataframe do pandas(a variavel pode ter outro nome)
print(df.head()) # Exibe as primeiras linhas do DataFrame
