from datetime import datetime
from bs4 import BeautifulSoup
import requests
import pandas as pd 

# Técnica de extração de dados utilizada para coletar dados de sites através de tags HTML e atributos CSS.

'''
Para fazer o web scraping, vamos utilizar as bibliotecas requests,
BeautifulSoup, pandas e datetime. As duas primeiras serão usadas para fazer a captura do conteúdo da página,
pandas para entregar os resultados em forma estruturada e datetime para marcar o dia e hora da extração.
'''

texto_string = requests.get('https://globoesporte.globo.com/').text   # link da extração
hora_extracao = datetime.now().strftime("%d-%m-%Y %H:%m:%S")  # registramos o horário da extração

bsp_texto = BeautifulSoup(texto_string, 'html.parser')
lista_noticias = bsp_texto.find_all('div', attrs={'class':'feed-post-body'}) # AS tags/div que queremos procurar

print('\n','Quantidade de manchetes = ', len(lista_noticias)) # mostra a quantidade de manchetes 
print('\n',lista_noticias[0].contents,'\n') # mostra as manchetes 

'''
Dentro dessa estrutura, procurando pelas tags corretas, vamos encontrar todas as informações que foram solicitadas.
Pela saída anterior podemos ver que a manchete ocupa a posição 2 da lista de conteúdos,
logo para guardar a manchete devemos fazer:
'''
print('\n',lista_noticias[0].contents[1].text.replace('"',"") ,'\n')  


# Para extração do link da noticia 
print('\n',lista_noticias[0].find('a').get('href'),'\n') # o '\n' no código e só para quebra a linha não e necessário para o código e de utilização minha 

'''
Para a descrição, da manchete como ela pode esta na terceira posição vamos ou em outra tag, vamos ter que testa
ambas e caso não esteja, então renornar None(nulo)
Veja a como fazer:
'''
descricao = None

# Verifica se há notícias na lista e se há pelo menos uma notícia
if lista_noticias and len(lista_noticias) > 0:
    # Obtém a primeira notícia da lista
    primeira_noticia = lista_noticias[0]
    
    # Tenta obter o texto da terceira parte da notícia
    if len(primeira_noticia.contents) > 2:
        descricao = primeira_noticia.contents[2].text
    # Caso a terceira parte não tenha o texto, tenta encontrar a tag 'div' com a classe 'bstn-related'
    elif (div_related := primeira_noticia.find('div', class_='bstn-related')):
        descricao = div_related.text
        
# Se após as tentativas ainda não tivermos uma descrição, será mantido como None

print('\n', descricao,'\n')


'''
Para extração da seção e do tempo decorrido, vamos acessar primeiro o atributo 'feed-post-metadata' e guardar em uma variável,
para em seguida, dentro desse novo subconjunto, localizar os atributos 'feed-post-datetime' e 'feed-post-metadata-section'.
Como existe a possibilidade dessa informação não existir,
precisamos garantir que somente acessaremos a propriedade text (linhas 6 e 7) caso tenha encontrando ("find").
Veja a seguir
'''

metadados = lista_noticias[0].find('div', attrs={'class':'feed-post-metadata'})

time_delta = metadados.find('span', attrs={'class': 'feed-post-datetime'})
secao = metadados.find('span', attrs={'class':'feed-post-metadata-section'})

time_delta = time_delta.text if time_delta else None
secao = secao.text if secao else None

print('\n', 'Time_delta = ', time_delta)
print('\n','seção = ', secao)


# veja que para noticia 0 extraunis tidas as informação solicitadas
'''
 mas precisamos extrair de todas, portanto cada extração deve ser feita dentro de uma estrutura de repetição.
 Para criar um DataFrame com os dados, vamos criar uma lista vazia e a cada iteração apendar uma tupla com as informações extraídas.
 Com essa lista, podemos criar nosso DataFrame, passando os dados e os nomes das colunas.
 Veja a seguir:
'''

# iniciar a lista vazia Dados
dados = []


# iniciar o loop  For para p interar cada elemento da lista_noticia
for noticia in lista_noticias:
    manchete = noticia.contents[1].text.replace('"',"")
    link = noticia.find('a').get('href')
    
    descricao = noticia.contents[2].text
    if not descricao:
        descricao = noticia.find('div', attrs={'class':'bstn-related'})
        descricao = descricao.text if descricao else None
        
    metadados = noticia.find('div', attrs={'class':'feed-post-metadata'})
    time_delta = metadados.find('span', attrs={'class':'feed-post-datetime'})
    secao = metadados.find('span', attrs={'class':'feed-post-metadata-section'})
    
    time_delta = time_delta.text if time_delta else None
    secao = secao.text if secao else None
    
    dados.append((manchete, descricao, link, secao, hora_extracao, time_delta))
    
df = pd.DataFrame(dados, columns=['manchete', 'descrição', 'link', 'seção', 'hora_extração', 'time_delta'])
df.head()

print('\n', df , '\n')