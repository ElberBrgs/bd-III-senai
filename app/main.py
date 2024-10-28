from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session
from os import system

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    #Solicitando dados para o usuário.

    while True:
        print("\n///Código/// \t ///Descrição///")
        print("1 \t Adicionar usuário.")
        print("2 \t Pesquisar um usuário.")
        print("3 \t Exibir usuários.")
    
        
        resposta = int(input("Informe o código desejado: "))
        system("cls || clear")
        
        match(resposta):
            case 1:
                print("\nAdicionando usuário.")
                nome = input("Digite seu nome: ")
                email = input("Digite seu email: ")
                senha = input("Digite sua senha: ")

                service.criar_usuario(nome=nome,email=email,senha=senha)
            case 2:
                print("\nListando todos os usuários cadastrados.")
                lista_usuarios = service.listar_todos_usuarios()
                for usuario in lista_usuarios:
                    print(f"Nome: {usuario.nome} - E-mail: {usuario.email} - Senha: {usuario.senha}")
                break
            case _:
                print("Código inválido, tente novamente.")            



if __name__ == "__main__":
    system("cls || clear")
    main()
