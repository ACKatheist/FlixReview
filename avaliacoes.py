import json

class AvaliacaoManager:
    def __init__(self, arquivo_json='avaliacoes.json'):
        self.arquivo_json = arquivo_json
        self.carregar_avaliacoes()

    def carregar_avaliacoes(self):
        try:
            with open(self.arquivo_json, 'r') as file:
                self.avaliacoes = json.load(file)
        except FileNotFoundError:
            self.avaliacoes = {}

    def salvar_avaliacoes(self):
        with open(self.arquivo_json, 'w') as file:
            json.dump(self.avaliacoes, file, indent=4)

    def adicionar_avaliacao(self, filme, avaliacao):
        if filme in self.avaliacoes:
            self.avaliacoes[filme]["avaliacoes"].append(avaliacao)
        else:
            self.avaliacoes[filme] = {"avaliacoes": [avaliacao]}
        self.salvar_avaliacoes()

    def calcular_media(self, filme):
        if filme in self.avaliacoes:
            avaliacoes = self.avaliacoes[filme]["avaliacoes"]
            if avaliacoes:
                media = sum(avaliacoes) / len(avaliacoes)
                return media
            else:
                return 0
        else:
            return None

    def validar_avaliacao(self, avaliacao):
        if 0 <= avaliacao <= 5:
            return True
        else:
            return False

def avaliar():
    avaliacao_manager = AvaliacaoManager()

    while True:
        print("\nEscolha uma opção:")
        print("1.Deixar uma avaliação")
        print("2.Listar médias das avaliações")
        print("3. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            filme = input("Digite o nome do filme: ")
            avaliacao = float(input("Digite a nota de 0 a 5 para o filme: "))
            if avaliacao_manager.validar_avaliacao(avaliacao):
                avaliacao_manager.adicionar_avaliacao(filme, avaliacao)
                print("Avaliação adicionada com sucesso!")
            else:
                print("A nota fornecida é inválida. Por favor, forneça uma nota entre 0 e 5.")
        elif opcao == '2':
            for filme, avaliacoes in avaliacao_manager.avaliacoes.items():
                media = avaliacao_manager.calcular_media(filme)
                print(f"Média de avaliações para o filme '{filme}': {media}")
        elif opcao == '3':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

#avaliar()
