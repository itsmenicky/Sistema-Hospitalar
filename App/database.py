from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

# Criando o banco de dados
engine = create_engine("sqlite:///server.db")

# Configurando sessão do SQLAlchemy
session = Session(engine)

# Criando classe da DeclarativeBase


class Base(DeclarativeBase):
    pass

# Função que inicializa o banco


def init_db():
    import models
    Base.metadata.create_all(bind=engine)
