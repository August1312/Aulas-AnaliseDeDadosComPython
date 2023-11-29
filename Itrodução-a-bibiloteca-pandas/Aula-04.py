# SELEÇÃO DE COLUNAS EM UM DATAFRAME

import pandas as pd

'''
Podemos realizar operações em colunas específicas de um DataFrame ou
ainda criar um novo objeto contendo somente as colunas que serão usadas em uma determinada análise.
Para selecionar uma coluna, as duas possíveis sintaxes são:

nome_df.nome_coluna
nome_df[nome_coluna]

A primeira forma é familiar aos desenvolvedores que utilizar a linguagem SQL,
porém ela não aceita colunas com espaços entre as palavras. Já a segunda aceita.
Se precisarmos selecionar mais do que uma coluna, então precisamos passar uma lista,
da seguinte forma: nome_df[['col1', 'col2', 'col3']],
se preferir a lista pode ser criada fora da seção e passada como parâmetro.

'''

dados = {
    'nomes': 'Howard Ian Peter Jonah Kellie'.split(),
    'cpfs' : '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),
    'emails' : 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split(),
    'idades' : [32, 22, 25, 29, 38]
}

df_dados = pd.DataFrame(dados)
df_dados1 = pd.DataFrame(dados)

df_uma_coluna = df_dados['idades']
print(type(df_uma_coluna))

print('Média de idades = ', df_uma_coluna.mean())
print(df_uma_coluna)

colunas = ['nomes', 'cpfs']
df_duas_colunas = df_dados1[colunas]
print(type(df_duas_colunas))
print(df_duas_colunas)