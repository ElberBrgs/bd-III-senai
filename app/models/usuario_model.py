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
        self.nome = self._verificar_valor_vazio(nome)
        self.email = self._verificar_valor_vazio(email)
        self.senha = self._verificar_valor_vazio(senha)

    def _verificar_valor_vazio(self,valor):
        if not isinstance(valor,str) or not valor.strip():
            raise ValueError("Insira um valor.")
        return valor

#Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)