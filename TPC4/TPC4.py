import random

lista = []
opcao = -1

while opcao != 0:

    print("       MENU       ")
    print("(1) Criar Lista")
    print("(2) Ler Lista")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) Está ordenada por ordem crescente")
    print("(8) Está ordenada por ordem decrescente")
    print("(9) Procura um elemento")
    print("(0) Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        n = int(input("Quantos números quer gerar? "))
        lista = []

        for i in range(n):
            numero = random.randint(1, 100)
            lista.append(numero)

        print("Lista criada:", lista)

    elif opcao == 2:
        n = int(input("Quantos números quer introduzir? "))
        lista = []

        for i in range(n):
            numero = int(input("Introduza um número: "))
            lista.append(numero)

        print("Lista criada:", lista)

    elif opcao == 3:
        if len(lista) > 0:
            soma = 0

            for numero in lista:
                soma = soma + numero

            print("Soma:", soma)
        else:
            print("A lista está vazia.")

    elif opcao == 4:
        if len(lista) > 0:
            soma = 0

            for numero in lista:
                soma = soma + numero

            media = soma / len(lista)
            print("Média:", media)
        else:
            print("A lista está vazia.")

    elif opcao == 5:
        if len(lista) > 0:
            maior = lista[0]

            for numero in lista:
                if numero > maior:
                    maior = numero

            print("Maior elemento:", maior)
        else:
            print("A lista está vazia.")

    elif opcao == 6:
        if len(lista) > 0:
            menor = lista[0]

            for numero in lista:
                if numero < menor:
                    menor = numero

            print("Menor elemento:", menor)
        else:
            print("A lista está vazia.")

    elif opcao == 7:
        if len(lista) > 0:
            crescente = True

            for i in range(len(lista) - 1):
                if lista[i] > lista[i + 1]:
                    crescente = False

            if crescente:
                print("Sim")
            else:
                print("Não")
        else:
            print("A lista está vazia.")

    elif opcao == 8:
        if len(lista) > 0:
            decrescente = True

            for i in range(len(lista) - 1):
                if lista[i] < lista[i + 1]:
                    decrescente = False

            if decrescente:
                print("Sim")
            else:
                print("Não")
        else:
            print("A lista está vazia.")

    elif opcao == 9:
        elemento = int(input("Que elemento pretende procurar? "))
        posicao = -1

        for i in range(len(lista)):
            if lista[i] == elemento and posicao == -1:
                posicao = i

        print("Posição:", posicao)

    elif opcao == 0:
        print("Lista final:", lista)
        print("Programa terminado.")

    else:
        print("Opção inválida.")