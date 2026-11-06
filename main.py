from erros_http import erros_http

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
        print("\n--- CONSULTA DE ERROS HTTP ---")
        print("Digite 'sair' para encerrar.")

        codigo = input("Digite um código HTTP: ").strip().lower()

        if codigo == "sair":
            print("Obrigado por utilizar o Smart API Assistant!")
            break

        consultar_erro(codigo)


apresentar_assistente()
iniciar_consultas()
