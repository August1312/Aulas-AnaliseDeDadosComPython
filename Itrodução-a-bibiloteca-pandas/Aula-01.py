# SERIES

import pandas as pd

'''
Para construir um objeto do tipo Series, precisamos utilizar o método Series() do pacote pandas.
O método possui o seguinte construtor: pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False).
Veja que todos os parâmetros possuem valores padrões (default) o que permite instanciar um objeto de diferentes formas.
Para endender cada parâmetro, a melhor fonte de informações é a documentação oficial:

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html.

'''

serie =  pd.Series(data=5)  # Cria uma Series com o valor a 


lista_nomes = 'Howard Ian Peter Jonah Kellie'.split() 
pd.Series(lista_nomes)   # Cria uma Series com uma lista de nomes


dados = {
    'nome1': 'Howard',
    'nome2': 'Ian',
    'nome3': 'Peter',
    'nome4': 'Jonah',
    'nome5': 'Kellie',
}
pd.Series(dados) # Cria uma Series com um dicionário


'''
Outra forma de construir a Series é passando os dados e os rótulos que desejamos usar. 
Veja no exemplo abaixo essa construção, na qual utilizaoms uma lista de supostos cpfs para rotular os valores da Series.

'''

cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
exemplo = pd.Series(lista_nomes, index=cpfs)


'''
Rotular as Series (e como veremos os DataFrames), é interessante para facilitar a localização e manipulação dos dados.
Por exemplo, se quiséssemos saber o nome da pessoa com cpf 111.111.111-11, poderíamos localizar facilmente essa informação com o atributo loc,
usando a seguinte sintaxe: series_dados.loc[rotulo], onde rótulo é índice a ser localizado. Veja o código a seguir na entrada 6,
criamos uma Series com a lista de nomes e guardados dentro uma variável chamada series_dados. Na linha 3, com o atributo loc,
localizamos a informação com índice '111.111.111-11'. Veremos mais sobre essa questão de filtrar informações, ao longo das aulas.
'''

series_dados = pd.Series(lista_nomes, index=cpfs)
exemplo2 = series_dados.loc['111.111.111-11']








print('\n')
print(serie)
print('\n')
print(lista_nomes)
print('\n')
print(dados)
print('\n')
print(exemplo)
print('\n')
print(exemplo2)