from models.usuario_model import Usuario
from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self,repository:UsuarioRepository):
        self.repository = repository

    def criar_usuario(self,nome:str,email:str,senha:str):
        try:
            usuario = Usuario(nome=nome,email=email,senha=senha)

            cadastrado = self.repository.pesquisar_usuario_por_email(usuario.email)

            if cadastrado:
                print("Usuário já cadastrado.")
                return

            self.repository.salvar_usuario(usuario)
            print("Usuário cadastrado com sucesso.") 
        except TypeError as error:
            print(f"Erro ao salvar o usuário: {error}")
        except Exception as error:       
            print(f"Ocorreu um erro inesperado: {error}")

    def listar_todos_usuarios(self):
        return self.repository.listar_usuarios()
    
    def pesquisar_usuario_unico(self):
        try:
            email_pesquisado = input("Digite o e-mail do usuário: ")
            cadastrado = self.repository.pesquisar_usuario_por_email(email=email_pesquisado)

            if cadastrado:
                print(f"Nome: {cadastrado.nome} - E-mail: {cadastrado.email} - Senha: {cadastrado.senha}")
                return
            else:
                print("Usuário não cadastrado.")
                return
        except TypeError as error:
            print(f"Erro ao pesquisar o usuário: {error}")
        except Exception as error:
            print(f"Erro inesperado: {error}")