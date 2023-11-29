'''
Um dos grandes recursos da biblioteca pandas é sua capacidade de fazer leitura de dados estruturados,
através de seus métodos, guardando em um DataFrame.
A biblioteca possui uma série de métodos "read", 
cuja sintaxe é: pandas.read_XXXXX() onde a sequência de X representa as diversas opções disponíveis.
'''
from requests import *
import pandas as pd 

url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'
dfs = pd.read_html(url)
df_bancos = dfs[0]

print(df_bancos.shape)
print(df_bancos.dtypes)

print(df_bancos.head())

print(type(dfs))
print(len(dfs))