#A partir de um dataframe existente seleciona a coluna especifica atravez do nome do dataframe e entre colchetes o nome da coluna, 
#e filtra a linha a partir de uma condição de acordo com os valores das linhas.
import pandas as pd

# Supondo que já tenha um DataFrame chamado pessoa_df
coluna_selecionada = pessoa_df['idade'] # Seleciona a coluna pelo nome dela no caso "idade"
linhas_filtradas = pessoa_df[pessoa_df['idade'] > 30] # Filtra as linhas onde a idade é maior que 30
print(coluna_selecionada) # Exibi a coluna "idade" 
print(linhas_filtradas) # Exibi as linhas filtradas
