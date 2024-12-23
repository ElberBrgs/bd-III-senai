import sys
import os

#Adiciona o diretório 'app' como diretório padrão
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from app.services.usuario_service import UsuarioService
from app.repositories.usuario_repository import UsuarioRepository
from app.config.database import Session

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    #Solicitando dados para o usuário.

    while True:
        print("\n///Código/// \t ///Descrição///")
        print("1 - Adicionar usuário.")
        print("2 - Pesquisar um usuário.")
        print("3 - Atualizar dados de um usuário.")
        print("4 - Excluir um usuário.")
        print("5 - Exibir todos os usuários cadastrados.")
        print("0 - Sair.")
    
        
        resposta = input("Informe o código desejado: ")
        os.system("cls || clear")
        
        match(resposta):
            case "1":
                print("\nAdicionando usuário.")
                nome = input("Digite seu nome: ")
                email = input("Digite seu email: ")
                senha = input("Digite sua senha: ")

                service.criar_usuario(nome=nome,email=email,senha=senha)
            case "2":
                service.pesquisar_usuario_unico()
            case "3":
                service.atualizar_dados_usuario()
            case "4":
                service.excluir_dados_usuario()
            case "5":
                print("\nListando todos os usuários cadastrados.")
                lista_usuarios = service.listar_todos_usuarios()
                for usuario in lista_usuarios:
                    print(f"Nome: {usuario.nome} - E-mail: {usuario.email} - Senha: {usuario.senha}")
            case "0":
                #Opcional : adicionar delay ao fechar terminal.    
                break
            case _:
                print("Código inválido, tente novamente.")            

    session.close()

if __name__ == "__main__":
    os.system("cls || clear")
    main()
