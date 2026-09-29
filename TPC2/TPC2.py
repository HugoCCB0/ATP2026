import random

opcao = int(input("Escolhe a modalidade (1 - computador adivinha / 2 - tu adivinhas): "))

if opcao == 1:
    limm = 0
    limM = 100

    num = random.randint(limm, limM)
    tentativas = 0

    resposta = ""

    while resposta != "Acertou!!":
        print(f"{num} é o número que eu pensei")

        tentativas += 1

        resposta = input("O número que pensaste é Maior, Menor ou Acertei? ")

        if resposta == "Maior":
            limm = num + 1
            num = random.randint(limm, limM)

        elif resposta == "Menor":
            limM = num - 1
            num = random.randint(limm, limM)

        elif resposta == "Acertei":
            print(f"Acertou! O número era {num}")
            print(f"Foram necessárias {tentativas} tentativas.")

        else:
            print("Resposta inválida!")


elif opcao == 2:

    num = random.randint(0, 100)

    n = int(input("Introduz um número de 0 a 100: "))
    tentativas = 1

    while n != num:

        if n < num:
            print("O número que pensei é Maior")

        else:
            print("O número que pensei é Menor")

        n = int(input("Tenta outra vez: "))
        tentativas += 1

    print("Acertei")
    print(f"Foram necessárias {tentativas} tentativas.")