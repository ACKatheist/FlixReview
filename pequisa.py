import pandas as pd
import jellyfish as jf
import json
import os
from avaliacoes import AvaliacaoManager
arquivo_json = 'comentarios.json'
avaliacao_json = 'avaliacoes.json'

def limpar_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class Pesquisa:
    def __init__(self, titulo = None):
        self.titulo = titulo
    def pesquisar(self):
        df = pd.read_csv('filme.csv', sep=',')
        df.drop_duplicates(inplace= True)
        df['titulo'] = df['titulo'].str.lower()
        lista_da_coluna = df['titulo'].tolist()
        lista_parametro = []
        for i in lista_da_coluna:
            parametro = jf.levenshtein_distance(i, self.titulo)
            lista_parametro.append(parametro)
        df_nome_parametro = pd.DataFrame(zip(lista_da_coluna, lista_parametro), columns = ['nome', 'parametro'])
        df_nome_parametro = df_nome_parametro.sort_values(by='parametro')
        print(df_nome_parametro['nome'][:10].to_string (index = False))
    def criarFilme(self):
        df = pd.read_csv('filme.csv', sep=',')
        print("Nome do filme: ")
        titulo = (input("").lower())
        limpar_console()
        print("Nome do diretor: ")
        diretor = (input("").lower())
        limpar_console()
        print("Nome do elenco: ")
        elenco = (input("").lower())
        limpar_console()
        print("Nome do pais: ")
        pais = (input("").lower())
        limpar_console()
        print("Breve sinopse: ")
        sinopse = (input("").lower())
        limpar_console()
        df.loc[len(df)] = (titulo, diretor, elenco, pais, sinopse)
        df.to_csv('filme.csv', index=False)
    def listarFilmes(self):
        df = pd.read_csv('filme.csv', sep=',')
        pd.set_option('display.max_rows', None)
        titulo = df['titulo']
        print(titulo)
        input('Pressione enter para continuar...')
        limpar_console()
        limpar_console()
        limpar_console()
    def atualizarFilme(self):
        df = pd.read_csv('filme.csv', sep=',')
        num = int(input("Qual a posição do filme (a posição pode se obitida em listar filmes): "))
        limpar_console()
        print("1. Título")
        print("2. Diretor")
        print("3. Elenco")
        print("4. País")
        print("5. Sinopse")
        print("6. Todos")
        print("7. Voltar")
        opc = int(input("Informe o que você deseja mudar: "))
        limpar_console()
        if opc == 1:
            print("Informe o novo nome do filme:")
            titulo = (input("").lower())
            df.loc[num,'titulo'] = (titulo)
            df.to_csv('filme.csv', index=False)
            input('Pressione enter para continuar...')
            limpar_console()
        elif opc == 2:
            print("Informe o novo nome do diretor:")
            diretor = (input("").lower())
            df.loc[num,'diretor'] = (diretor)
            df.to_csv('filme.csv', index=False)
            input('Pressione enter para continuar...')
            limpar_console()
        elif opc == 3:
            print("Informe o nome do novo elenco:")
            elenco = (input("").lower())
            df.loc[num,'elenco'] = (elenco)
            df.to_csv('filme.csv', index=False)
            input('Pressione enter para continuar...')
            limpar_console()
        elif opc == 4:
            print("Informe o nome do novo país:")
            pais = (input("").lower())
            df.loc[num,'pais'] = (pais)
            df.to_csv('filme.csv', index=False)
            input('Pressione enter para continuar...')
            limpar_console()
        elif opc == 5:
            print("Informe a nova sinopse:")
            sinopse = (input("").lower())
            df.loc[num,'sinopse'] = (sinopse)
            df.to_csv('filme.csv', index=False)
            input('Pressione enter para continuar...')
            limpar_console()
        elif opc == 6:
            print("Informe o novo nome do filme:")
            titulo = (input("").lower())
            print("Informe o novo nome do diretor:")
            diretor = (input("").lower())
            print("Informe o nome do novo elenco:")
            elenco = (input("").lower())
            print("Informe o nome do novo país:")
            pais = (input("").lower())
            print("Informe a nova sinopse:")
            sinopse = (input("").lower())
            df.loc[num] = (titulo, diretor, elenco, pais, sinopse)
            df.to_csv('filme.csv', index=False)
            limpar_console()
        else:
            print("saindo...")
            input('Pressione enter para continuar...')
            limpar_console()
    def deletarFilme(self):
        df = pd.read_csv('filme.csv', sep=',')
        num = int(input("qual a posição do filme (a posição pode se obitida em listar filmes): "))
        df.drop(index=num, inplace=True)
        df.to_csv('filme.csv', index=False)
        print('Filme deletado com sucesso!')
        input('Pressione enter para continuar...')
        limpar_console()
    def infofilme(self):
        df = pd.read_csv('filme.csv', sep=',')
        nome = input("Sobre qual filme deseja saber mais? ")
        limpar_console()
        linha = df[df['titulo'] == nome]
        for index, value in linha.iterrows():
            for col in df.columns:
                print(f"{col}: {value[col]}")
        with open('comentarios.json', 'r') as file:
            dados = json.load(file)
        for item in dados:
            if item['Id'] == nome:
                print(f"Comentario: {item['Comentarios']}")
                media = AvaliacaoManager()
                mediac = media.calcular_media(nome)
                print(f"Média: {mediac}")