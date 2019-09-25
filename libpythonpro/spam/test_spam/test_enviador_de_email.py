'''
    Utilizando TDD - Baby Steps
'''
import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido

'''def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None
'''


#decorator
@pytest.mark.parametrize(
    'remetente',
    ['eduardorumbels@hotmail.com', 'foo@bar.com.br', 'testemail@mail.com', 'pytest@teste.com.br']

) #é uma feature para parametrizar um teste
def test_remetente(remetente):
    enviador=Enviador()
    destinatarios = ['eduardorumbels@hotmail.com', 'foo@bar.com.br']

    resultado = enviador.enviar(
        remetente,
        'eduardo.rumbels@gmail.com',
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossum aberta'
    )
    assert remetente in resultado




# decorator
@pytest.mark.parametrize(
    'remetente',
    ['', 'eduardo']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()

    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'eduardo.rumbels@gmail.com',
            'Cursos Python Pro',
            'Primeira turma Guido Von Rossum aberta'
        )
