from libpythonpro.spam.modelos import Usuario

'''

**Estrutura dos testes**

def test_salvar_usuario():
    {
    
    conexao = Conexao()
    sessao = conexao.gerar_sessao() 
    
    } - Fase de inicialização (Setup)
    
    
    usuario = Usuario(nome='Eduardo')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)    
    
    {
    
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar() 
    
    } - Fase de finalização (Tear Down)

'''


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Eduardo', email='eduardorumbels@hotmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Eduardo', email='eduardorumbels@hotmail.com'),
                Usuario(nome='Querido', email='eduardorumbels@hotmail.com')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()