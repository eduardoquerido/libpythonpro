import pytest

from libpythonpro.spam.db import Conexao
'''
O arquivo conftest.py é um modo de disponibilizar as fixtures para todos os módulos.
'''

@pytest.fixture(scope='session') #scope='function' é o padrão, já o scope='module' ele irá executar apenas no módulo em que ela está
def conexao():                   #scope='session', se vários outros módulos estiverem utilizando essa fixture, ela será executada apenas uma vez
    #Setup
    conexao_obj = Conexao()
    yield conexao_obj
    #Tear Down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    #Setup
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    #Tear Down
    sessao_obj.roll_back()
    sessao_obj.fechar()