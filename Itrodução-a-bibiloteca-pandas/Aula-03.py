#  DATAFRAME
import pandas as pd


'''
Para construir um objeto do tipo DataFrame, precisamos utilizar o método DataFrame() do pacote pandas.
O método possui o seguinte construtor:
pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False).
'''

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
lista_cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
lista_emails = 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split()
lista_idades = [32, 22, 25, 29, 38]

exemplo = pd.DataFrame(lista_nomes, columns=['nome'])
exemplo2 = pd.DataFrame(lista_nomes, columns=['nome'], index=lista_cpfs)


dados = list(zip(lista_nomes, lista_cpfs, lista_idades, lista_emails)) # cria uma lista de tuplas
exemplo3 = pd.DataFrame(dados, columns=['nome', 'cpfs', 'idade', 'email'])


# CONSTRUTOR DATAFRAME COM DICIONÁRIO

'''
DataFrames também podem ser construídos a partir de estruturas de dados do tipo dicionário.
Cada chave será uma coluna e pode ter atribuída uma lista de valores.
Obs: cada chave deve estar associada a uma lista de mesmo tamanho. Na entrada 12,
criamos nosso dicionário de dados, veja que cada chave possui uma lista de mesmo tamanho e criamos nosso DataFrame,
passando o dicionário como fonte de dados. Dessa forma o construtor já consegue identificar o nome das colunas.
'''


# EXTRAINDO INFORMAÇÕES DE UM DATAFRAME

'''
Como já mencionamos, cada objeto possui seus próprios atributos e métodos,
logo, embora Series e DataFrame tenham recursos em comum, eles também possuem suas particularidades.
No DataFrame temos o método info() que mostra quantas linhas e colunas existem. Também exibe o tipo de cada coluna e quanto valores não nulos existem ali.
Esse método também retorna uma informação sobre a quantidade de memória RAM essa estrutura está ocupando. Faça a leitura dos comentários e veja o que cada atributo e método retorna.
'''

dados = {
    'nomes': 'Howard Ian Peter Jonah Kellie'.split(),
    'cpfs' : '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),
    'emails' : 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split(),
    'idades' : [32, 22, 25, 29, 38]
}

df_dados = pd.DataFrame(dados)

print('\nInformações do DataFrame:\n')
print(df_dados.info()) # Apresenta informações sobre a estrutura do DF

print('\nQuantidade de linhas e colunas = ', df_dados.shape) # Retorna uma tupla com o número de linhas e colunas
print('\nTipo de dados:\n', df_dados.dtypes) # Retorna o tipo de dados, para cada coluna, se for misto será object

print('\nQual o menor valor de cada coluna?\n', df_dados.min()) # Extrai o menor de cada coluna 
print('\nQual o maior valor?\n', df_dados.max()) # Extrai o valor máximo e cada coluna 
print('\nQual a média aritmética?\n', df_dados.mean()) # Extrai a média aritmética de cada coluna numérica
print('\nQual o desvio padrão?\n', df_dados.std()) # Extrai o desvio padrão de cada coluna numérica
print('\nQual a mediana?\n', df_dados.median()) # Extrai a mediana de cada coluna numérica

print('\nResumo:\n', df_dados.describe()) # Exibe um resumo

df_dados.head() # Exibe os 5 primeiros registros do DataFrame



