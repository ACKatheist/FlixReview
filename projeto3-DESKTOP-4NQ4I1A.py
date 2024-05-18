import os # importando o módulo "os" para interagir com o sistema e verificar se um arquivo existe
import pandas as pd # importando o módulo do "pandas" com o apelido de pd (pandas usado muito para análise e manipulação de dados)
from pequisa import Pesquisa # importando a classe Pesquisa definida em um arquivo chamado "pesquisa.py"

    #### CRIANDO A CLASSE ####

class RegistroUsuario:             # Definindo a classe "RegistroUsuario que vai ser responsável por gerenciar o registro e login de usuários"
    
    def __init__(self):            # Definindo o método especial "__init__", que é chamado quando uma instância da classe é criada. (este metódo inicializa os atributos da classe)
        self.arquivo = 'registro_usuarios.csv'         # Definindo o atributo "arquivo", que armazena o nome do arquivo CSV onde será armazenado os dados dos úsuarios
    
        if os.path.isfile(self.arquivo):       # Verificar se o arquivo CSV existe
            self.df = pd.read_csv(self.arquivo)     # essa linha vai verificar se o arquivo existe, caso ele exista ele lê o arquivo CSV para um dataframe do pandas chamado "self.df"
        else:
            self.df = pd.DataFrame(columns=['Nome', 'Email', 'Senha']) # cria um data frame vazio com as colunas 'Nome','Email','Senha'
            
   #### REGISTRAR USUARIO ####

    def registrar_usuario(self, nome, email, senha):    # Define o método "registrar_usuario", que vai registrar um novo usuário com um nome, email e senha fornecidos
        if '@' not in email:          # Verifica se o email fornecido contém o caractere "@" (verificação básica de validade do email)
            print("O email fornecido é inválido.")        # se o email n for válido, imprime uma mensagem de erro
            return            # encerra o método se o email n for válido
        
        if email in self.df['Email'].values:            # ele vai verificar se o email fornecido já está presente na coluna do 'Email' do dataFrame
            print("Este email já está cadastrado.")         # caso o email já esteja cadastrado, imprime uma mensagem de erro
        else:
            novo_registro = pd.DataFrame({'Nome': [nome], 'Email': [email], 'Senha': [senha]})     # Cria um novo dataFrame chamado "novo_registro", contendo as informações do novo usuário.
            self.df = pd.concat([self.df, novo_registro], ignore_index=True)         # Concatena o novo registro ao dataFrame existente, ignorando os índices existentes.
            self.df.to_csv(self.arquivo, index=False)             # salva o dataFrame atualizado como um arquivo CSV, sobrescrevendo o arquivo existente
            print("Usuário registrado com sucesso.")            # imprime uma mensagem de sucesso após o registro do usuário

   #### LOGIN DO USUARIO ####

    def fazer_login(self, email, senha):                 # Definindo o método "fazer_login", que permite com que o usuário faça login usando seu email e senha
        usuario = self.df[(self.df['Email'] == email) & (self.df['Senha'] == senha)]         # filtra o dataFrame para encontrar uma linha que corresponde ao email e senha fornecidos
        if not usuario.empty:                      # verifica se o dataFrame resultante não está vazio, ou seja, se o usuário foi encontrado 
            print("Login bem-sucedido.")                # Caso o usuário tenha sido encontrado, imprime uma mensagem de sucesso
            print("Bem-vindo,", usuario['Nome'].values[0])          # imprime o nome do usuário que fez o login bem sucedido
            return True                  # retorna verdadeiro para indicar que o login foi bem sucedido
                
        else:
            print("Email ou senha incorretos. Tente novamente.")   # caso o usuário não for encontrado, imprime uma mensagem de erro indicando que o email ou senha fornecidos estão incorretos
            return False            # retorna falso para indicar que o login não foi bem-sucedido


registro = RegistroUsuario()      # cria uma instância da classe "RegistroUsuario", que será usada para lidar com o registro e login de usuários

logado = False          # define uma variável "logado", como "false" para controlar o estado do login do usuário

while not logado:           # entra em um loop enquanto o usuário não estiver logado
    


    print("\n1. Registrar usuário")
    print("2. Fazer login")                   # EXIBE AS OPÇÕES DISPONÍVEIS PARA O USUÁRIO
    print("3. Sair")

    escolha = input("Escolha uma opção: ")    # SOLICITA AO USUÁRIO QUE ESCOLHA UMA OPÇÃO E ARMAZENA A ESCOLHA NA VARIÁVEL "escolha"
    

    if escolha == "1":    # caso o usuário escolha a opção 1 :
        nome = input("Digite seu nome: ")     # SOLICITA AO USUÁRIO SEU NOME
        email = input("Digite seu email: ")   # SOLICITA AO USUÁRIO SEU EMAIL
        senha = input("Digite sua senha: ")   # SOLICITA AO USUÁRIO SUA SENHA
        registro.registrar_usuario(nome, email, senha)         # chama o método "registrar_usuario" para registrar um novo usuário com as informações fornecidas

    elif escolha == "2":    # caso o usuário escolha a opção 2 :
        while True: # antes de tudo aq tem um loop infinito para solicitar o email e senha até que o login e seja bem-sucedido
         email = input("Digite seu email: ")       # SOLICITA AO USUÁRIO SEU EMAIL
         senha = input("Digite sua senha: ")     # SOLICITA AO USUÁRIO SUA SENHA
         if registro.fazer_login(email, senha):            # chama o método "fazer_login" para tentar fazer login com as informações fornecidas
           logado = True         # define "logado" como verdadeiro para indicar que o usuário está logado
           break       # sai do loop após o login bem-sucedido

    elif escolha == "3":       # caso a opção escolhida for sair
        print("Saindo...")        # imprime uma mensagem indicando que o programa está saindo
        exit()     # encerra o programa
    else: 
        print("Opção inválida. Tente novamente.")  # se a escolha não corresponder a nenhuma das opções válidas, imprime uma mensagem de erro indicando que a opção escolhida é inválida

print("nome do filme:")
filme = Pesquisa(input("").lower())           # APÓS O LOGIN BEM-SUCEDIDO, SEGUE PARA A PARTE DA PESQUISA DO FILME
filme.pesquisar()


