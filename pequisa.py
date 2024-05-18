import numpy as np
import pandas as pd
import jellyfish as jf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



### Método de pesquisa usando o algoritmo de levenshtein ###

class Pesquisa:
    def __init__(self, palavra):
        self.palavra = palavra

    def pesquisar(self):
        ### Dataframe ###
        df2 = pd.read_csv('filmes.csv', sep=',')

        ### Pequeno tratamento de dados ###
        df2.drop_duplicates(inplace= True)

        ### Convertendo para minúsculo ###
        df2['title'] = df2['title'].str.lower()

        ### Transformo em lista para fazer a comparação ###
        lista_da_coluna = df2['title'].tolist()

        ### Definindo a lista para salvar os parametros ###
        lista_parametro = []

        ### Loop que faz a comparação com o algoritimo de levenshtein ###
        for i in lista_da_coluna:
            parametro = jf.levenshtein_distance(i, self.palavra)
            lista_parametro.append(parametro)

        ### Definindo o data frame de novo para facilitar a exibição e organizando a ordem ###
        df_nome_parametro = pd.DataFrame(zip(lista_da_coluna, lista_parametro), columns = ['nome', 'parametro'])
        df_nome_parametro = df_nome_parametro.sort_values(by='parametro')
        
        ### Outro df para a recomendacao ###
        df = pd.read_csv('filmes.csv', sep=',')

        ### Pequeno tratamento de dados ###
        df.drop_duplicates(inplace= True)

        ### Criando minha coluna com os parametros para a recomendacao ###
        df['parametros'] = df['listed_in'] + df['title'] + str(df['director']) + str(df['cast']) + str(df['country'])

        ### Deixando os titulos em letra minuscula ###
        df['title'] = df['title'].str.lower()

        ### Usando a função tfidf pra vetorizar os meus dados com uma biblioteca de machinelearning ###
        vec = TfidfVectorizer()
        tfidf = vec.fit_transform(df['parametros'].apply(lambda x: np.str_(x)))

        ### Usando a similaridade entre os cossenos dos vetores gerados ###
        sim = cosine_similarity(tfidf)

        ### Transformando em data frame ###
        sim_df = pd.DataFrame(sim, columns=df['title'], index=df['title'])
        
        ### Criando a variavel pra recomendação com base no primeiro resultado da pesquisa ###
        reco = df_nome_parametro.iat[0, 0]

        ### recomendacao organizada em uma dataframe pronto para exibição ###
        recomenda_df = pd.DataFrame(sim_df[reco].sort_values(ascending=False))
        recomenda = pd.DataFrame(recomenda_df.index[1:10])
        print(df_nome_parametro['nome'][:10].to_string (index = False))
        print(recomenda['title'][:10].to_string (index = False))

print("nome do filme:")
filme = Pesquisa(input("").lower())
filme.pesquisar()