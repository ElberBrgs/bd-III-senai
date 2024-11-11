import pytest

from app.models.usuario_model import Usuario

@pytest.fixture
def usuario_valido():
    return Usuario("João","joao@email.com","123")

def test_nome_valido(usuario_valido):
    assert usuario_valido.nome == "João"

def test_email_valido(usuario_valido):
    assert usuario_valido.email == "joao@email.com"

def test_senha_valida(usuario_valido):
    assert usuario_valido.senha == "123"

def test_nome_vazio():
    with pytest.raises(ValueError,match = "Insira um valor."):
        Usuario("","joao@email.com","123")

def test_email_vazio():
    with pytest.raises(ValueError,match = "Insira um valor."):
        Usuario("João","","123")

def test_senha_vazia():
    with pytest.raises(ValueError,match = "Insira um valor."):
        Usuario("João","joao@email.com","")

def test_nome_invalido():
    with pytest.raises(TypeError, match= "Tipo inválido."):
        Usuario(256,"joao@email.com","123")

def test_email_invalido():
    with pytest.raises(TypeError, match= "Tipo inválido."):
        Usuario(256,789,"123")

def test_senha_invalida():
    with pytest.raises(TypeError, match= "Tipo inválido."):
        Usuario(256,"joao@email.com",123)
