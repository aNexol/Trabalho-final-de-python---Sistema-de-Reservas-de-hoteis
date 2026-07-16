from view.login_view import tela_login
from view.menu_view import mostrar_menu

from controller.login_controller import validar_login
from controller.reserva_controller import realizar_checkin
from controller.quarto_controller import listar_quartos

usuario_logado = None

while True:

    usuario, senha = tela_login()

    if validar_login(usuario, senha):

        usuario_logado = usuario
        break

    print("Usuário ou senha inválidos!")

while True:

    opcao = mostrar_menu()

    if opcao == "1":

        realizar_checkin()

    elif opcao == "2":

        listar_quartos()

    elif opcao == "0":

        print("Encerrando sistema...")
        break

    input("\nENTER para continuar...")