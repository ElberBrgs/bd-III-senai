from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import declarative_base
from app.config.database import db

Base = declarative_base()

class Usuario(Base):
    #Definindo características da tabela no banco de dados.
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True,autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150))
    senha = Column(String(150))

    #Definindo características da classe.
    def __init__(self,nome:str,email:str,senha:str):
        self.nome = self._verificar_tipo_e_valor(nome)
        self.email = self._verificar_tipo_e_valor(email)
        self.senha = self._verificar_tipo_e_valor(senha)

    def _verificar_tipo_e_valor(self,valor):
        if not isinstance(valor,str):
            raise TypeError("Tipo inválido.")
        if not valor.strip():
            raise ValueError("Insira um valor.")
        return valor
    
#Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)