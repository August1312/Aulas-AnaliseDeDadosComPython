# EXEMPLIFICANDO
'''Vamos utilizar tudo que já aprendemos e fazer uma atividade de raspagem web (web scraping).
Vamos acessar a seguinte página de notícias do jornal New York Times: https://nyti.ms/3aHRu2D. 
A partir dessa fonte de informações vamos trabalhar para criar um DataFrame contendo o dia da notícia, 
o comentário que foi feito, a explicação que foi dada e o link da notícia.

Vamos começar nossa raspagem utilizando um recurso que já nos é familiar, 
a biblioteca requests! Fazer a extração da notícia com o requestes.get() convertendo tudo para uma única string,
por isso vamos usar a propriedade text. Na linha 4, da entrada 16 imprimimos os 100 primeiros caracteres do texto que capturamos.
Veja que foi lido o conteúdo HTML da página.
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd 


texto_string = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html').text
print(texto_string[:100])


bsp_texto = BeautifulSoup(texto_string, 'html.parser')
lista_noticias = bsp_texto.find_all('span', attrs={'class':'short-desc'})

print(type(bsp_texto))
print(type(lista_noticias))
print(lista_noticias[5])

lista_noticias[5].contents

'''
Linha 1: Criamos uma lista vazia.
Linha 4: O código noticia.contents[0] retorna: <strong>Jan. 25
</strong>, ao acessar a propriedade text, eliminamos as tags, então temos Jan. 25. Usamos a função strip() para eliminar espaço em branco na string e concatenamos com o ano.
Linha 5: O código contents[1] retorna: "“You had millions of people that now aren't insured anymore.” " usamos o strip() para eliminar espaços em branco e a função replace para substituir os caracteres especiais por nada.
Linha 6: O código noticia.contents[2] retorna: <a href="https://www.nytimes.com/2017/03/13/us/politics/fact-check-trump-obamacare-health-care.html" target="_blank"
>(The real number is less than 1 million, according to the Urban Institute.)</a></span>, ao acessar a propriedade text, eliminamos as tags então temos (The real number is less than 1 million, according to the Urban Institute.), o qual ajustamos para elimar espaços e os parênteses.
Linha 7: o código noticia.find('a')['href'] retorna: https://www.nytimes.com/2017/03/13/us/politics/fact-check-trump-obamacare-health-care.html
Apendamos a nossa lista de dados uma tupla com as quatro informações que extraímos.
'''


dados = []

for noticia in lista_noticias:
    data = noticia.contents[0].text.strip() + ', 2017' # Dessa informação <strong>Jan. 25 </strong> vai extrair Jan. 25, 2017
    comentario = noticia.contents[1].strip().replace("“", '').replace("”", '')
    explicacao = noticia.contents[2].text.strip().replace("(", '').replace(")", '')
    url = noticia.find('a')['href']
    dados.append((data, comentario, explicacao, url))

print(dados[1])


df_noticias = pd.DataFrame(dados, columns=['data', 'comentário', 'explicação', 'url'])

print(df_noticias.shape)
print(df_noticias.dtypes)
print(df_noticias.head())