import requests


def buscar_avatar(usuario):
    '''
    Busca o avatar de um usuário no Github

    :param usuario: str com o nome de usuário no github
    :return: str com link do avatar
    '''

    url = f'http://appi.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']
