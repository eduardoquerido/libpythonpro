
#biblioteca para mockar o enviador
from unittest.mock import Mock
#biblioteca de testes
import pytest

#importações
from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


'''
class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_emails_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente , destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_emails_enviados += 1

A classe Mock acima pode ser utilizada com a biblioteca from unittest.mock import Mock
'''



@pytest.mark.parametrize(
    'usuarios',
    [
        [
                Usuario(nome='Eduardo', email='eduardorumbels@hotmail.com'),
                Usuario(nome='Querido', email='eduardorumbels@hotmail.com')
        ],
        [
                Usuario(nome='Eduardo', email='eduardorumbels@hotmail.com')
        ]
    ]

)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam= EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'eduardorumbels@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos',
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Eduardo', email='eduardorumbels@hotmail.com')
    sessao.salvar(usuario)
    enviador = Mock() #utilizando a biblioteca unittest.mock
    enviador_de_spam= EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'querido@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos',
    )
    enviador.enviar.assert_called_once_with(
        'querido@hotmail.com',
        'eduardorumbels@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
   )