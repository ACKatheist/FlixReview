import os 
import re 
import pandas as pd 
from pequisa import Pesquisa 
import comentarios
from avaliacoes import AvaliacaoManager

def limpar_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def validar_email(email):

    padrao_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(padrao_email, email) is not None

def validar_senha(senha):

    padrao_senha = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return re.match(padrao_senha, senha) is not None

class RegistroUsuario:             
    
    def __init__(self):            
        self.arquivo = 'registro_usuarios.csv'         
    
        if os.path.isfile(self.arquivo):       
            self.df = pd.read_csv(self.arquivo)     
        else:
            self.df = pd.DataFrame(columns=['Nome', 'Email', 'Senha', 'Admin']) 
            admin = pd.DataFrame({'Nome': ['Admin'], 'Email': ['admin@'], 'Senha': ['admin'], 'Admin': [True]})
            self.df = pd.concat([self.df, admin], ignore_index=True)
            self.df.to_csv(self.arquivo, index=False)
            

    def registrar_usuario(self, nome, email, senha,):   
        
        if not validar_email(email):         
            print("O email fornecido é inválido. Certifique-se de que o email esteja no formato correto (exemplo: nome@exemplo.com).")
            input("Pressione Enter para tentar novamente...")        
            return            
        
        if not validar_senha(senha):
            print("A senha forneciada deve conter pelo menos 8 caracteres, incluindo uma letra maiúscula, uma letra minúscula, um número e um caractere especial.")
            input("Pressione Enter para tentar novamente...")
            return
        
        if email in self.df['Email'].values:            
            print("Este email já está cadastrado.")
            input("Pressione Enter para tentar novamante...")        
        else:
            novo_registro = pd.DataFrame({'Nome': [nome], 'Email': [email], 'Senha': [senha], 'Admin':[False]})     
            self.df = pd.concat([self.df, novo_registro], ignore_index=True)         
            self.df.to_csv(self.arquivo, index=False)             
            print("Usuário registrado com sucesso.")            
            input("Pressione Enter para continuar...")


    def fazer_login(self, email, senha):                 

        usuario = self.df[(self.df['Email'] == email) & (self.df['Senha'] == senha)]         
        if not usuario.empty:                      
            limpar_console()
            print("Login bem-sucedido.")                
            print("Bem-vindo,", usuario['Nome'].values[0])  
            admin_logado = usuario['Admin'].values[0]
            input("Pressione Enter para continuar...")
            limpar_console()

            if admin_logado:
                if email == 'admin@' and senha == 'admin':
                    print("Você está logado como admin.")
                    input("Pressione Enter para continuar...")
                    limpar_console()
                    while True:
                        print("\n1. Ações Filme!")
                        print("2. Ações Usuários!")
                        print("3. Ações Comentários!")
                        print("4. Encerrar o Programa!")
                        escolha = int(input("Escolha uma opção: "))
                        limpar_console()
                        if escolha == 1:
                            while True:
                                print("\n1. Criar filme!")
                                print("2. Ver lista de filmes!")
                                print("3. Atualizar filme!")
                                print("4. Deletar filme!")
                                print("5. Voltar!")
                                escolha1 = int(input("Escolha uma opção: "))
                                limpar_console()
                                if escolha1 == 1:
                                    obra = Pesquisa()
                                    obra.criarFilme()
                                elif escolha1 == 2:
                                    obra = Pesquisa()
                                    obra.listarFilmes()
                                elif escolha1 == 3:
                                    obra = Pesquisa()
                                    obra.atualizarFilme()
                                elif escolha1 == 4:
                                    obra = Pesquisa()
                                    obra.deletarFilme()
                                else:
                                    print("Saindo...")
                                    input('Pressione enter para continuar...')
                                    limpar_console()
                                    break
                        elif escolha == 2:
                            print("\n1. Criar usuário!")
                            print("2. Ver lista de usuários!")
                            print("3. Atualizar usuário!")
                            print("4. Deletar usuário!")
                            print("5. Voltar!")
                            escolha2 = int(input("Escolha uma opção: "))
                            limpar_console()
                            if escolha2 == 1:
                                nome1 = input("Digite seu nome: ")     
                                limpar_console()
                                email1 = input("Digite seu email: ")
                                limpar_console()   
                                senha1 = input("Digite sua senha: ")  
                                limpar_console() 
                                registro.registrar_usuario(nome1, email1, senha1,)
                            elif escolha2 == 2:
                                df = pd.read_csv('registro_usuarios.csv', sep=',')
                                pd.set_option('display.max_rows', None)
                                colunas = ['Nome', 'Email', 'Senha']
                                print(df[colunas])
                                input('Pressione enter para continuar...')
                                limpar_console()
                            elif escolha2 == 4:
                                df = pd.read_csv('registro_usuarios.csv', sep=',')
                                num = int(input("qual a posição do usuario (a posição pode se obitida em listar usuarios, use 0 para voltar): "))
                                if num  ==  0:
                                    print("voltando...")
                                else:
                                    df.drop(index=num, inplace=True)
                                    df.to_csv('registro_usuarios.csv', index=False)
                                    print('Usuário deletado com sucesso!')
                                    input('Pressione enter para continuar...')
                                    limpar_console()
                            elif escolha2 == 3:
                                df = pd.read_csv('registro_usuarios.csv', sep=',')
                                num = int(input("Qual a posição do usuário (a posição pode se obtida em listar usuários, use 0 para voltar): "))
                                limpar_console()
                                print("1. Nome!")
                                print("2. Email!")
                                print("3. Senha!")
                                print("4. Todos!")
                                print("5. Voltar!")
                                opc = int(input("Qual informação quer mudar: "))
                                limpar_console()
                                if opc == 1:
                                    print("Novo nome: ")
                                    nome = (input(""))
                                    df.loc[num,'Nome'] = (nome)
                                    df.to_csv('registro_usuarios.csv', index=False)
                                    print('Alteração Concluída com sucesso!')
                                    input('Pressione enter para continuar...')
                                    limpar_console()
                                elif opc == 2:
                                    print("Novo email: ")
                                    email2 = (input(""))
                                    df.loc[num,'Email'] = (email2)
                                    df.to_csv('registro_usuarios.csv', index=False)
                                    print('Alteração Concluída com sucesso!')
                                    input('Pressione enter para continuar...')
                                    limpar_console()
                                elif opc == 3:
                                    print("Nova senha: ")
                                    senha2 = (input(""))
                                    df.loc[num,'Senha'] = (senha2)
                                    df.to_csv('registro_usuarios.csv', index=False)
                                    print('Alteração Concluída com sucesso!')
                                    input('Pressione enter para continuar...')
                                    limpar_console()
                                elif opc == 4:
                                    print("Novo nome: ")
                                    nome = (input(""))
                                    print("Novo email: ")
                                    email2 = (input(""))
                                    print("Nova senha: ")
                                    senha2 = (input(""))
                                    df.loc[num] = (nome, email2, senha2)
                                    df.to_csv('registro_usuarios.csv', index=False)
                                    limpar_console()
                                    print('Alteração Concluída com sucesso!')
                                    input('Pressione enter para continuar...')
                                    limpar_console()
                                else:
                                    print("saindo...")
                        elif escolha == 3:
                            comentarios.comentar()
                        else:
                            print('Encerrando...')
                            exit()
            else:
                while True:
                    print("\n1. Pesquisar Filme!")
                    print("2. Comentar e avaliar filme!")
                    print("3. Encerrar o programa!")
                    escolha = int(input("Escolha uma opção: "))
                    limpar_console()
                    if escolha  == 1:
                        print("Nome do filme:")
                        filme = Pesquisa(input("").lower()) 
                        limpar_console()
                        filme.pesquisar()
                        print("\n1. Saber mais sobre algum filme!")
                        print("2. Voltar!")
                        escolha = int(input("Escolha uma opção: "))
                        limpar_console()
                        if escolha == 1:
                            obra = Pesquisa(filme)
                            filme.pesquisar()
                            obra.infofilme()
                            input('Pressione enter para continuar...')
                            limpar_console()
                        elif escolha == 2:
                            print("Saindo...")
                    elif escolha == 2:
                        nomefilme = input("Digite o nome  do filme:  ")
                        limpar_console()
                        comentario = input("Digite seu comentário: ")
                        comentarios.adicionar_comentario(comentario, nomefilme)
                        limpar_console()
                        avaliacao = float(input("Digite a nota de 0 a 5 para o filme: "))
                        manager =  AvaliacaoManager()
                        if manager.validar_avaliacao(avaliacao):
                            manager.adicionar_avaliacao(nomefilme, avaliacao)
                            limpar_console()
                            print("Avaliação adicionada com sucesso!")
                            input("Pressione Enter para continuar...")
                            limpar_console()
                    elif escolha == 3:
                        print("Saindo...")
                        exit()
                    else:
                        print("Opção inválida!")       
        else:
            print("Email ou senha incorretos.")   
            input("Pressione Enter para tentar novamente...")
            return False, False            

registro = RegistroUsuario()      

logado = False          
admin_logado = False

while not logado:           
    limpar_console()


    print("\n1. Registrar usuário")
    print("2. Fazer login")                   
    print("3. Sair")

    escolha = input("Escolha uma opção: ")  
    limpar_console()  
    

    if escolha == "1":    
        limpar_console()
        nome = input("Digite seu nome: ")
        limpar_console()     
        email = input("Digite seu email: ")
        limpar_console()   
        senha = input("Digite sua senha: ")
        limpar_console()
        registro.registrar_usuario(nome, email, senha,)       

    elif escolha == "2":    
        while True: 
         limpar_console()
         email = input("Digite seu email: ")  
         limpar_console()     
         senha = input("Digite sua senha: ")     
         logado, admin_logado = registro.fazer_login(email, senha)            
         if logado:        
             break       
        

    elif escolha == "3":       
        print("Saindo...")        
        exit()     
    else: 
        print("Opção inválida. Tente novamente.") 
        input("Pressione Enter para tentar novamente...")
