from model.quartos import quartos

def realizar_checkin():

    quarto = int(input("Número do quarto: "))

    if quartos[quarto] == "Livre":

        quartos[quarto] = "Ocupado"

        print("Check-in realizado!")

    else:

        print("Quarto ocupado!")