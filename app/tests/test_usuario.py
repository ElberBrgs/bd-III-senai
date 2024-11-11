import pytest

from app.models.usuario_model import Usuario

@pytest.fixture
def usuario_valido():
    return Usuario("João","joao@email.com","123")

def nome_valido(usuario_valido):
    assert usuario_valido.nome == "João"

def test_nome_vazio():
    with pytest.raises(ValueError,match = "Insira um nome."):
        Usuario("","joao@email.com","123")

def test_email_vazio():
    with pytest.raises(ValueError,match = "Insira um e-mail."):
        Usuario("João","","123")

def test_senha_vazia():
    with pytest.raises(ValueError,match = "Insira uma senha."):
        Usuario("João","joao@email.com","")


