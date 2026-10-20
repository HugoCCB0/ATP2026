def menu():
    print("\n--- MENU DE OPERAÇÕES ---")
    print("1: Criar uma turma[cite: 1]")
    print("2: Inserir um aluno na turma[cite: 1]")
    print("3: Listar a turma[cite: 1]")
    print("4: Consultar um aluno por id[cite: 1]")
    print("8: Guardar a turma em ficheiro[cite: 1]")
    print("9: Carregar uma turma dum ficheiro[cite: 1]")
    print("0: Sair da aplicação[cite: 1]")

def main():
    turma = []  
    opcao = ""
    
    while opcao != "0":
        menu()
        opcao = input("Escolhe uma opção: ")
        
        if opcao == "1":
            turma = []
            print("Turma criada com sucesso!")
            
        elif opcao == "2":
            nome = input("Nome do aluno: ")
            aluno_id = input("ID do aluno: ")
            nota_tpc = float(input("Nota TPC: "))
            nota_proj = float(input("Nota Proj: "))
            nota_teste = float(input("Nota Teste: "))
            aluno = (nome, aluno_id, [nota_tpc, nota_proj, nota_teste])  
            turma.append(aluno)
            print("Aluno inserido com sucesso!")
            
        elif opcao == "3":
            print("\n--- LISTA DA TURMA ---")
            i = 0
            while i < len(turma):
                aluno = turma[i]
                print(f"Nome: {aluno[0]} | ID: {aluno[1]} | Notas: TPC={aluno[2][0]}, Proj={aluno[2][1]}, Teste={aluno[2][2]}")
                i = i + 1
                
        elif opcao == "4":
            procura_id = input("Insere o ID do aluno a consultar: ")
            encontrado = False
            i = 0
            while i < len(turma):
                aluno = turma[i]
                if aluno[1] == procura_id:
                    print(f"Aluno encontrado -> Nome: {aluno[0]} | Notas: {aluno[2]}")
                    encontrado = True
                i = i + 1
            if not encontrado:
                print("Aluno não encontrado.")
                
        elif opcao == "8":
            nome_ficheiro = input("Nome do ficheiro para guardar: ")
            ficheiro = open(nome_ficheiro, "w", encoding="utf-8")
            i = 0
            while i < len(turma):
                aluno = turma[i]
                linha = f"{aluno[0]},{aluno[1]},{aluno[2][0]},{aluno[2][1]},{aluno[2][2]}\n"
                ficheiro.write(linha)
                i = i + 1
            ficheiro.close()
            print("Turma guardada com sucesso!")
            
        elif opcao == "9":
            nome_ficheiro = input("Nome do ficheiro para carregar: ")
            ficheiro = open(nome_ficheiro, "r", encoding="utf-8")
            turma = []
            linhas = ficheiro.readlines()
            i = 0
            while i < len(linhas):
                linha = linhas[i].strip()
                if linha != "":
                    partes = linha.split(",")
                    nome = partes[0]
                    aluno_id = partes[1]
                    notas = [float(partes[2]), float(partes[3]), float(partes[4])]
                    aluno = (nome, aluno_id, notas)
                    turma.append(aluno)
                i = i + 1
            ficheiro.close()
            print("Turma carregada com sucesso!")
            
        elif opcao == "0":
            print("A sair da aplicação...")
            
        else:
            print("Opção inválida. Tenta novamente.")

if __name__ == "__main__":
    main()