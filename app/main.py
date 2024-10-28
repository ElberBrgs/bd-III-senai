from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session
from os import system

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    #Solicitando dados para o usuário.
    print("\nAdicionando usuário.")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    service.criar_usuario(nome=nome,email=email,senha=senha)

    #Listar todos os usuários cadastrados.
    print("\nListando todos os usuários cadastrados.")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"Nome: {usuario.nome} - E-mail: {usuario.email} - Senha: {usuario.senha}")

if __name__ == "__main__":
    system("cls || clear")
    main()
