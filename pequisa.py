import numpy as np
import pandas as pd
import jellyfish as jf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



### Método de pesquisa usando o algoritmo de levenshtein ###

class Pesquisa:
    def __init__(self, titulo = None):
        self.titulo = titulo
    def pesquisar(self):
        df2 = pd.read_csv('filme.csv', sep=',')
        df2.drop_duplicates(inplace= True)
        df2['titulo'] = df2['titulo'].str.lower()
        lista_da_coluna = df2['titulo'].tolist()
        lista_parametro = []
        for i in lista_da_coluna:
            parametro = jf.levenshtein_distance(i, self.titulo)
            lista_parametro.append(parametro)
        df_nome_parametro = pd.DataFrame(zip(lista_da_coluna, lista_parametro), columns = ['nome', 'parametro'])
        df_nome_parametro = df_nome_parametro.sort_values(by='parametro')
        print(df_nome_parametro['nome'][:10].to_string (index = False))
    def criarFilme(self):
        df = pd.read_csv('filme.csv', sep=',')
        print("nome do filme:")
        titulo = (input("").lower())
        print("nome do diretor:")
        diretor = (input("").lower())
        print("nome do elenco:")
        elenco = (input("").lower())
        print("nome do pais:")
        pais = (input("").lower())
        print("breve sinopse:")
        sinopse = (input("").lower())
        df.loc[len(df)] = (titulo, diretor, elenco, pais, sinopse)
        df.to_csv('filme.csv', index=False)
    def listarFilmes(self):
        df = pd.read_csv('filme.csv', sep=',')
        pd.set_option('display.max_rows', None)
        print(df['titulo'])
    def atualizarFilme(self):
        df = pd.read_csv('filme.csv', sep=',')
        num = int(input("qual a posição do filme (a posição pode se obitida em listar filmes): "))
        print("1: titulo")
        print("2: diretor")
        print("3: elenco")
        print("4: pais")
        print("5: sinopse")
        print("6: todos")
        opc = int(input(""))
        if opc == 1:
            print("novo nome do filme:")
            titulo = (input("").lower())
            df.loc[num,'titulo'] = (titulo)
            df.to_csv('filme.csv', index=False)
        elif opc == 2:
            print("novo nome do diretor:")
            diretor = (input("").lower())
            df.loc[num,'diretor'] = (diretor)
            df.to_csv('filme.csv', index=False)
        elif opc == 3:
            print("novo nome do elenco:")
            elenco = (input("").lower())
            df.loc[num,'elenco'] = (elenco)
            df.to_csv('filme.csv', index=False)
        elif opc == 4:
            print("novo nome do pais:")
            pais = (input("").lower())
            df.loc[num,'pais'] = (pais)
            df.to_csv('filme.csv', index=False)
        elif opc == 5:
            print("nova sinopse:")
            sinopse = (input("").lower())
            df.loc[num,'sinopse'] = (sinopse)
            df.to_csv('filme.csv', index=False)
        elif opc == 6:
            print("novo nome do filme:")
            titulo = (input("").lower())
            print("novo nome do diretor:")
            diretor = (input("").lower())
            print("novo nome do elenco:")
            elenco = (input("").lower())
            print("novo nome do pais:")
            pais = (input("").lower())
            print("nova sinopse:")
            sinopse = (input("").lower())
            df.loc[num] = (titulo, diretor, elenco, pais, sinopse)
            df.to_csv('filme.csv', index=False)
        else:
            print("opcao nao existente")
    def deletarFilme(self):
        df = pd.read_csv('filme.csv', sep=',')
        num = int(input("qual a posição do filme (a posição pode se obitida em listar filmes): "))
        df.drop(index=num, inplace=True)
        df.to_csv('filme.csv', index=False)

#obra = Pesquisa()
#obra.pesquisas()

#obra = Pesquisa()
#obra.criarFilme()

#obra = Pesquisa()
#obra.listarFilmes()

#obra = Pesquisa()
#obra.atualizarFilme()

#obra = Pesquisa()
#obra.deletarFilme()