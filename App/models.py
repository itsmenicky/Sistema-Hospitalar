from sqlalchemy import Column, Integer, String
from database import Base

# Criando entidade Paciente


class Paciente(Base):
    __tablename__ = "PACIENTE"
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    cpf = Column('CPF', String(255))
    idade = Column('IDADE', Integer)

    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

# Criando entidade Médico


class Medico(Base):
    __tablename__ = "MEDICO"
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))
    crm = Column('CRM', String(255))
    especializacao = Column('ESPECIALIZACAO', String(255))

    def __init__(self, nome, crm, especializacao):
        self.nome = nome
        self.crm = crm
        self.especializacao = especializacao

# Criando entidade Exame


class Exame(Base):
    __tablename__ = "EXAME"
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    id_medico = Column('ID__MEDICO', Integer)
    id_paciente = Column('ID_PACIENTE', Integer)
    descricao = Column('DESCRICAO', String(255))
    resultado = Column('RESULTADO', String(255))

    def __init__(self, id_medico, id_paciente, descricao, resultado):
        self.id_medico = id_medico
        self.id_paciente = id_paciente
        self.descricao = descricao
        self.resultado = resultado
