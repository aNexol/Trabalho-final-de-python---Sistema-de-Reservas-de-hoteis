from model.quartos import quartos

def listar_quartos():

    print("\nQUARTOS")

    for numero, status in quartos.items():
        print(f"Quarto {numero}: {status}")