from models import *
from database import session

# Função responsável pelo cadastro de pacientes


def cadastrar_paciente(nome, cpf, idade):
    novo_paciente = Paciente(nome, cpf, idade)
    session.add(novo_paciente)
    session.commit()
    print("Paciente cadastrado com sucesso!")
    session.close()

# Função responsável pelo cadastro de médicos


def cadastrar_medico(nome, crm, especializacao):
    novo__medico = Medico(nome, crm, especializacao)
    session.add(novo__medico)
    session.commit()
    print("Médico cadastrado com sucesso!")
    session.close()

# Função responsável pelo cadastro de exames


def cadastrar_exame(crm_medico, cpf_paciente, descricao, resultado):
    medico = session.query(Medico).filter(Medico.crm == crm_medico).first()
    if not medico:
        print("Médico com o CRM informado não encontrado no sistema.")
        return
    paciente = session.query(Paciente).filter(
        Paciente.cpf == cpf_paciente).first()
    if not paciente:
        print("Paciente com o CPF informado não encontrado no sistema.")
        return
    novo_exame = Exame(medico.id, paciente.id, descricao, resultado)
    session.add(novo_exame)
    session.commit()
    print("Exame cadastrado com sucesso!")
    session.close()

# Função responsável por consultar exames por paciente


def consultar_exames_paciente(cpf_paciente):
    paciente = session.query(Paciente).filter(
        Paciente.cpf == cpf_paciente).first()
    if not paciente:
        print("Paciente com o CPF informado não encontrado.")
        return
    for item in session.query(Exame).filter(Exame.id_paciente == paciente.id):
        print("-"*10)
        print(f"\n     Exame n° {item.id}")
        print(f"     Id do médico responsável: {item.id_medico}")
        print(f"     Id do paciente examinado: {item.id_paciente}")
        print(f"     Descrição do exame: {item.descricao}")
        print(f"     Resultado do exame: {item.resultado}\n")
        print("-"*10)
