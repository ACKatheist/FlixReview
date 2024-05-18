import os
import pandas as pd
from pequisa import Pesquisa

class RegistroUsuario:
    
    def __init__(self):
        self.arquivo = 'registro_usuarios.csv'
       
        if os.path.isfile(self.arquivo):
            self.df = pd.read_csv(self.arquivo)
        else:
            self.df = pd.DataFrame(columns=['Nome', 'Email', 'Senha'])
            

    def registrar_usuario(self, nome, email, senha):
        if '@' not in email:
            print("O email fornecido é inválido.")
            return
        
        if email in self.df['Email'].values:
            print("Este email já está cadastrado.")
        else:
            novo_registro = pd.DataFrame({'Nome': [nome], 'Email': [email], 'Senha': [senha]})
            self.df = pd.concat([self.df, novo_registro], ignore_index=True)
            self.df.to_csv(self.arquivo, index=False)
            print("Usuário registrado com sucesso.")



    def fazer_login(self, email, senha):
        usuario = self.df[(self.df['Email'] == email) & (self.df['Senha'] == senha)]
        if not usuario.empty:
            print("Login bem-sucedido.")
            print("Bem-vindo,", usuario['Nome'].values[0])
                
        else:
            print("Email ou senha incorretos. Tente novamente.")


registro = RegistroUsuario()



while True:
    


    print("\n1. Registrar usuário")
    print("2. Fazer login")
    print("3. Sair")

    escolha = input("Escolha uma opção: ")
    

    if escolha == "1":
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        registro.registrar_usuario(nome, email, senha)
    elif escolha == "2":
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        registro.fazer_login(email, senha)
        break

    elif escolha == "3":
        print("Saindo...")
        exit()
    else:
        print("Opção inválida. Tente novamente.")

print("nome do filme:")
filme = Pesquisa(input("").lower())
filme.pesquisar()