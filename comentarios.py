import csv
import json

arquivo_json = 'comentarios.json'
arquivo_csv = 'comentarios.csv'

def carregar_comentarios():
    try:
        with open(arquivo_json, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def salvar_comentarios(comentarios):
    with open(arquivo_json, 'w') as file:
        json.dump(comentarios, file, indent=4)

def exportar_para_csv(comentarios):
    with open(arquivo_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Id", "Comentario"])
        for comentario in comentarios:
            writer.writerow([comentario["Id"], comentario["Comentario"]])

def adicionar_comentario(comentario):
    comentarios = carregar_comentarios()
    comentario_id = len(comentarios) + 1
    comentarios.append({"Id": comentario_id, "Comentario": comentario})
    salvar_comentarios(comentarios)
    exportar_para_csv(comentarios)
    print(f"Comentário adicionado com ID {comentario_id}")

def listar_comentarios():
    comentarios = carregar_comentarios()
    return comentarios

def excluir_comentario(comentario_id):
    comentarios = carregar_comentarios()
    comentarios = [c for c in comentarios if c["Id"] != int(comentario_id)]
    salvar_comentarios(comentarios)
    exportar_para_csv(comentarios)
    print(f"Comentário com ID {comentario_id} excluído")

def mostrar_menu():
    print("\nEscolha uma opção:")
    print("1. Adicionar comentário")
    print("2. Listar comentários")
    print("3. Excluir comentário")
    print("4. Sair")

def comentar():
    while True:
        mostrar_menu()
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == '1':
            comentario = input("Digite seu comentário: ")
            adicionar_comentario(comentario)
        elif opcao == '2':
            comentarios = listar_comentarios()
            print("Comentários:")
            for comentario in comentarios:
                print(f"ID: {comentario['Id']}, Comentário: {comentario['Comentario']}")
        elif opcao == '3':
            comentario_id = input("Digite o ID do comentário a ser excluído: ")
            excluir_comentario(comentario_id)
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


comentar()
