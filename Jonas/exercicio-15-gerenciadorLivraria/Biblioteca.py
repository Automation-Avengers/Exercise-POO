import json
import csv
import pickle

from functools import reduce
from Livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)
    
    def listar_livros_por_autor(self, autor):
        return list(filter(lambda livro: livro.autor == autor, self.livros))
    
    def listar_titulos(self):
        return list(map(lambda livro: livro._titulo, self.livros))

    def contar_livros_por_genero(self, genero):
        return reduce(lambda contador, livro: contador + 1 if livro._genero == genero else contador, self.livros,0)
        
    def salvar_txt(self, nome_arquivo="Biblioteca.txt"):
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_txt:
            for livro in self.livros:
                arquivo_txt.write(f"{livro._titulo},{livro._autor},{livro._ano},{livro._genero}\n")
        print(f"Dados salvos em {nome_arquivo}.")

    def carregar_txt(self, nome_arquivo="Biblioteca.txt"):
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_txt:
            self.livros = []
            for linha in arquivo_txt:
                titulo, autor, ano, genero = linha.strip().split(',')
                self.livros.append(Livro(titulo, autor, int(ano), genero))
        print(f"Dados carregados de {nome_arquivo}.")
    
    def salvar_json(self, nome_arquivo = "Biblioteca.json"):
        dados = [{"titulo": livro._titulo, "autor": livro._autor, "ano": livro._ano, "genero": livro._genero} for livro in self.livros]
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json)
        print(f"Dados salvos em {nome_arquivo}.")

    def carregar_json(self, nome_arquivo="Biblioteca.json"):
        with open(nome_arquivo, "r", encoding='utf-8') as arquivo_json:
            dados = json.load(arquivo_json)
            self.livro = [Livro(**livro) for livro in dados]
        print(f"Dados carregados de {nome_arquivo}.")

    def salvar_csv(self, nome_arquivo="Biblioteca.csv"):
        with open(nome_arquivo, "w", newline="", encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(["Título", "Autor", "Ano", "Gênero"])
            for livro in self.livros:
                escritor.writerow([livro._titulo, livro._autor, livro._ano, livro._genero])
        print(f"Dados salvos em {nome_arquivo}.")

    def carregar_csv(self, nome_arquivo="Biblioteca.csv"):
        with open(nome_arquivo, "r", encoding='utf-8') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            next(leitor)
            self.livros = [Livro(linha[0], linha[1], int(linha[2]), linha[3]) for linha in leitor]
        print(f"Dados carregados de {nome_arquivo}.")

    def salvar_pickle(self, nome_arquivo="Biblioteca.pkl"):
        with open(nome_arquivo, "wb") as arquivo:
            pickle.dump(self.livros, arquivo)
        print(f"Dados salvos em {nome_arquivo}.")

    def carregar_pickle(self, nome_arquivo="Biblioteca.pkl"):
        with open(nome_arquivo, "rb") as arquivo:
            self.livros = pickle.load(arquivo)
        print(f"Dados carregados de {nome_arquivo}.")

    def backup(self, formato):
        if formato == "json":
            self.salvar_json()
        elif formato == "pickle":
            self.salvar_pickle()
        else:
            print(f"Formato {formato} não suportado para backup.")

    def filtrar_livros(self, ano=None, genero=None):
        return list(filter(lambda livro: (ano is None or livro._ano == ano) and (genero is None or livro._genero == genero), self.livros))