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
            if admin_logado:
                if email == 'admin@' and senha == 'admin':
                    print("Você está logado como admin.")
                    while True:
                        print("\n1.acoes filme")
                        print("2.acoes usuarios")
                        print("3.acoes comentarios")
                        print("4.parar programa")
                        escolha = int(input("Escolha uma opção: "))
                        if escolha == 1:
                            while True:
                                print("\n1.criar filme")
                                print("2.ver lista de filmes")
                                print("3.atualizar filme")
                                print("4.deletar filme")
                                print("5.voltar")
                                escolha1 = int(input("Escolha uma opção: "))
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
                                    break
                        elif escolha == 2:
                            print("\n1.criar usuario")
                            print("2.ver lista de usuarios")
                            print("3.atualizar usuario")
                            print("4.deletar usuario")
                            print("5.voltar")
                            escolha2 = int(input("Escolha uma opção: "))
                            if escolha2 == 1:
                                nome1 = input("Digite seu nome: ")     
                                email1 = input("Digite seu email: ")   
                                senha1 = input("Digite sua senha: ")   
                                registro.registrar_usuario(nome1, email1, senha1,)
                            elif escolha2 == 2:
                                df = pd.read_csv('registro_usuarios.csv', sep=',')
                                pd.set_option('display.max_rows', None)
                                print(df['nome','email','senha'])
                            elif escolha2 == 4:
                                df = pd.read_csv('registro_usuarios.csv', sep=',')
                                num = int(input("qual a posição do usuario (a posição pode se obitida em listar usuarios, use 0 para voltar): "))
                                if num  ==  0:
                                    print("voltando...")
                                else:
                                    df.drop(index=num, inplace=True)
                                    df.to_csv('registro_usuarios.csv', index=False)
                            elif escolha2 == 3:
                                df = pd.read_csv('registro_usuarios.csv', sep=',')
                                num = int(input("qual a posição do filme (a posição pode se obitida em listar filmes): "))
                                print("1.nome")
                                print("2.email")
                                print("3.senha")
                                print("4.todos")
                                print("5.voltar")
                                opc = int(input("qual argumento quer mudar: "))
                                if opc == 1:
                                    print("novo nome: ")
                                    nome = (input(""))
                                    df.loc[num,'Nome'] = (nome)
                                    df.to_csv('registro_usuarios.csv', index=False)
                                elif opc == 2:
                                    print("novo email: ")
                                    email2 = (input(""))
                                    df.loc[num,'Email'] = (email2)
                                    df.to_csv('registro_usuarios.csv', index=False)
                                elif opc == 3:
                                    print("nova senha: ")
                                    senha2 = (input(""))
                                    df.loc[num,'Senha'] = (senha2)
                                    df.to_csv('registro_usuarios.csv', index=False)
                                elif opc == 4:
                                    print("novo nome: ")
                                    nome = (input(""))
                                    print("novo email: ")
                                    email2 = (input(""))
                                    print("nova senha: ")
                                    senha2 = (input(""))
                                    df.loc[num] = (nome, email2, senha2)
                                    df.to_csv('registro_usuarios.csv', index=False)
                                else:
                                    print("saindo...")
                        elif escolha == 3:
                            comentarios.comentar()
                        else:
                            exit()
            else:
                while True:
                    print("\n1.pesquisar filme")
                    print("2.comentar e avaliar filme")
                    print("3.encerrar programa")
                    escolha = int(input("Escolha uma opção: "))
                    if escolha  == 1:
                        print("Nome do filme:")
                        filme = Pesquisa(input("").lower())  
                        filme.pesquisar()
                        print("\n1.ver informacoes de um filme")
                        print("2.voltar")
                        escolha = int(input("Escolha uma opção: "))
                        if escolha == 1:
                            obra = Pesquisa()
                            obra.infofilme()
                        elif escolha == 2:
                            print("Saindo...")
                    elif escolha == 2:
                        nomefilme = input("Digite o nome  do filme: ")
                        comentario = input("Digite seu comentário: ")
                        comentarios.adicionar_comentario(comentario, nomefilme)
                        avaliacao = float(input("Digite a nota de 0 a 5 para o filme: "))
                        manager =  AvaliacaoManager()
                        if manager.validar_avaliacao(avaliacao):
                            manager.adicionar_avaliacao(nomefilme, avaliacao)
                            print("Avaliação adicionada com sucesso!")
                    elif escolha == 3:
                        print("Saindo...")
                        exit()
                    else:
                        print("opcao invalida")       
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
    

    if escolha == "1":    
        limpar_console()
        nome = input("Digite seu nome: ")     
        email = input("Digite seu email: ")   
        senha = input("Digite sua senha: ")   
        registro.registrar_usuario(nome, email, senha,)       

    elif escolha == "2":    
        while True: 
         limpar_console()
         email = input("Digite seu email: ")       
         senha = input("Digite sua senha: ")     
         logado, admin_logado = registro.fazer_login(email, senha)            
         if logado:        
             break       
        

    elif escolha == "3":       
        print("Saindo...")        
        exit()     
    else: 
        print("Opção inválida. Tente novamente.") 
        input("Pressione Enter para continuar...")
