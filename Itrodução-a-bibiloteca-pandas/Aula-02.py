# EXTRAINDO INFORMAÇÕES DE UMA SERIES

import pandas as pd

'''
Verifique no comentário a frente de cada comando, o que ele faz.
Vale a pena ressaltar a diferença entre o atributo shape e o método count().
O primeiro verifica quantas linhas a Series possui (quantos índices),
já o segundo, conta quantos dados não nulos existem.
'''

series_dados = pd.Series([10.2, -1, None, 15, 23.4])
print('\n')
print('Quantidade de linhas = ', series_dados.shape) # Retorna uma tupla com o número de linhas

print('Tipo de dados', series_dados.dtypes) # Retorna o tipo de dados, se for misto será object

print('Os valores são únicos?', series_dados.is_unique) # Verifica se os valores são únicos (sem duplicações)

print('Existem valores nulos?', series_dados.hasnans) # Verifica se existem valores nulos

print('Quantos valores existem?', series_dados.count()) # Conta quantas valores existem (excluí os nulos)

print('Qual o menor valor?', series_dados.min()) # Extrai o menor valor da Series (nesse caso os dados precisam ser do mesmo tipo)

print('Qual o maior valor?', series_dados.max()) # Extrai o valor máximo, com a mesma condição do mínimo

print('Qual a média aritmética?', series_dados.mean()) # Extrai a média aritmética de uma Series numérica

print('Qual o desvio padrão?', series_dados.std()) # Extrai o desvio padrão de uma Series numérica

print('Qual a mediana?', series_dados.median()) # Extrai a mediana de uma Series numérica

print('\nResumo:\n', series_dados.describe()) # Exibe um resumo sobre os dados na Series

