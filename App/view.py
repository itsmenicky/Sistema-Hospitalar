from controllers import *
import os
import time


def menu_principal():
    def printLogo():
        os.system('cls')
        print("           ________           ")
        time.sleep(0.3)
        print("          |        |          ")
        time.sleep(0.3)
        print("          |        |          ")
        time.sleep(0.3)
        print("          |        |          ")
        time.sleep(0.3)
        print("__________          __________")
        time.sleep(0.3)
        print("|                            |")
        time.sleep(0.3)
        print("|                            |")
        time.sleep(0.3)
        print("|_________          _________|")
        time.sleep(0.3)
        print("          |        |         ")
        time.sleep(0.3)
        print("          |        |         ")
        time.sleep(0.3)
        print("          |        |         ")
        time.sleep(0.3)
        print("          |________|         ")
        time.sleep(0.3)

    os.system('cls')
    print("\n")
    print("=" * 50)
    print("   _    _      _ _        ")
    print("  | |  | |    | | |       ")
    print("  | |__| | ___| | | ___   ")
    print("  |  __  |/ _ \ | |/ _ \  ")
    print("  | |  | |  __/ | | (_) | ")
    print("  |_|  |_|\___|_|_|\___/  ")
    print("                          ")
    print("=" * 50)
    print("\n")
    time.sleep(2)
    printLogo()

    while True:
        os.system('cls')
        print("+-"*20)
        print("       Oque iremos realizar hoje?")
        print("\n          1 - Cadastrar Médico   ")
        print("          2 - Cadastrar Paciente ")
        print("          3 - Cadastrar exame    ")
        print("          4 - Consultar exames   \n")
        print("+-"*20)
        try:
            escolha = int(input("\n\n-> "))
        except ValueError:
            print("Escolha uma opção válida de acordo com o número correspondente!")
            time.sleep(1)
            continue

        if escolha == 1:
            printLogo()
            os.system('cls')
            print("+-"*5 + "Cadastro de médico\n")
            nome_medico = input("Nome do medico -> ")
            crm_medico = input("CRM do medico -> ")
            especializacao_medico = input("Especializacao do medico -> ")
            cadastrar_medico(nome_medico, crm_medico, especializacao_medico)
            time.sleep(5)
        elif escolha == 2:
            printLogo()
            os.system('cls')
            print("+-"*5 + "Cadastro de paciente\n")
            nome_paciente = input("Nome do paciente -> ")
            cpf_paciente = input("CPF do paciente -> ")
            idade_paciente = int(input("Idade do paciente -> "))
            cadastrar_paciente(nome_paciente, cpf_paciente, idade_paciente)
            time.sleep(5)
        elif escolha == 3:
            printLogo()
            os.system('cls')
            print("+-"*5 + "Cadastro de exame\n")
            crm_medico = input("Insira o crm do medico -> ")
            cpf_paciente = input("Insira o cpf do paciente -> ")
            descricao = input("Insira a descricao do exame -> ")
            resultado = input("Insira o resultado do exame -> ")
            cadastrar_exame(crm_medico, cpf_paciente, descricao, resultado)
            time.sleep(5)
        elif escolha == 4:
            printLogo()
            os.system('cls')
            print("+-"*5 + "Consulta por exames\n")
            cpf_paciente = input("Insira o cpf do paciente a ser consultado -> ")
            consultar_exames_paciente(cpf_paciente)
            time.sleep(10)
        else:
            print("Opção inválida!")
            time.sleep(1)
            continue
