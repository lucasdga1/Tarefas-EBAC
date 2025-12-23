import requests
from bs4 import BeautifulSoup
# Pega o site e trabalha o código
site = requests.get('https://books.toscrape.com/')
livros = BeautifulSoup(site.text, 'lxml')

cont_livros = 0
lista_livros = []

# Lista cada título dentro do código de cada livro
for livro in livros.find_all('article', class_= 'product_pod'):
    titulo = livro.h3.a['title']
    preco = livro.find('p', class_= 'price_color').text.strip()

    catalogo = {'Título': titulo, 'Preço': preco}
    lista_livros.append(catalogo)
    cont_livros +=1

# Imprime a lista um a um pelo catálogo
for i, catalogo in enumerate(lista_livros, start=1):
    print(f"{i}. {catalogo['Título']} - {catalogo['Preço']}")

print(f"Foram encontrados {cont_livros} livros.")