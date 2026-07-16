from model import usuarios

def validar_login(usuario, senha):

    if usuario in usuarios:
        return usuarios[usuario] == senha

    return False