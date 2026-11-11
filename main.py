from erros_http import erros_http
from assistente_ia import perguntar_ia

def apresentar_assistente():
    print("================================")
    print("      SMART API ASSISTANT")
    print("================================")

    nome = input("Qual é o seu nome? ")
    print(f"Olá, {nome}! Vamos aprender sobre APIs.")


def consultar_erro(codigo):
    if codigo in erros_http:
        erro = erros_http[codigo]

        print(f"HTTP {codigo} - {erro['nome']}")
        print(erro["descricao"])
        print(f"Possível solução: {erro['solucao']}")

    else:
        print("Código ainda não cadastrado no assistente.")



def iniciar_consultas():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Consultar erro HTTP")
        print("2 - Perguntar para a IA")
        print("3 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            codigo = input("Digite um código HTTP: ").strip()
            consultar_erro(codigo)

        elif opcao == "2":
            pergunta = input("Digite sua pergunta para a IA: ").strip()

            if pergunta:
                print("\nConsultando a inteligência artificial...")
                resposta = perguntar_ia(pergunta)
                print(f"\nResposta da IA:\n{resposta}")
            else:
                print("Digite uma pergunta válida.")

        elif opcao == "3":
            print("Obrigado por utilizar o Smart API Assistant!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    apresentar_assistente()
    iniciar_consultas()
