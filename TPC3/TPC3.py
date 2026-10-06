def jogada_computador(total):

    if total < 100 and 100 - total <= 10:
        return 100 - total

    for numero in range(1, 11):
        novo_total = total + numero

        if novo_total > 100:
            continue

        if novo_total % 11 == 0:
            return numero

    return 1


def jogar_computador_primeiro():

    total = 0

    while total < 100:

        numero = jogada_computador(total)

        total += numero

        print("Computador adicionou:", numero)
        print("Total:", total)

        if total == 100:
            print("O COMPUTADOR GANHOU!")
            return

        while True:
            try:
                numero = int(input("Escolhe um número de 1 a 10: "))

                if 1 <= numero <= 10 and total + numero <= 100:
                    break

                print("Jogada inválida!")

            except ValueError:
                print("Introduz um número válido.")

        total += numero

        print("Jogador adicionou:", numero)
        print("Total:", total)

        if total == 100:
            print("O JOGADOR GANHOU!")
            return


def jogar_computador_segundo():

    total = 0

    while total < 100:

        while True:
            try:
                numero = int(input("Escolhe um número de 1 a 10: "))

                if 1 <= numero <= 10 and total + numero <= 100:
                    break

                print("Jogada inválida!")

            except ValueError:
                print("Introduz um número válido.")

        total += numero

        print("Jogador adicionou:", numero)
        print("Total:", total)

        if total == 100:
            print("O JOGADOR GANHOU!")
            return

        numero = jogada_computador(total)

        total += numero

        print("Computador adicionou:", numero)
        print("Total:", total)

        if total == 100:
            print("O COMPUTADOR GANHOU!")
            return


def menu():

    while True:

        print("1 - Computador joga primeiro")
        print("2 - Computador joga em segundo")

        opcao = input("Escolhe uma opção: ")

        if opcao == "1":
            jogar_computador_primeiro()

        elif opcao == "2":
            jogar_computador_segundo()

        else:
            print("Opção inválida!")

menu()