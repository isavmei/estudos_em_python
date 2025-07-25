#webscrap e automação de textos 

import requests
from bs4 import BeautifulSoup
import openai

url = "site necessário pra ler como a wikipédia"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

conteudo = soup.find('div', id='mw-content-text') #esse aqui busca os conteudos dentro da div do site. é bom procurar... pode estar em class, table... depende do que se quer.

texto = conteudo.get_text() #esse extrai as informações apenas em texto. se não tiver ele, eu recebo tudo de dentro da div do mw-content-text

with open("resumo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(texto)

openai.api_key = "chave API!" 

resposta = openai.ChatCompletion.create( #envia o texto a ser lido. 
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Resumidor de textos WEB"},
        {"role": "user", "content": f"{texto}"} #saida de texto dele 
    ]
)
resumo = resposta.choices[0].message.content #extrai o conteúdo do resumo da resposta da API

with open("resumo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(resumo)

#para que rode, é necessário criar uma chave api da open ia; e para isso se deve entrar no site e se inscrever. 