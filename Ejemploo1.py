def multiplicacion(multiplicando,multiplicador):
    producto = multiplicando * multiplicador
    return producto

if __name__=="__main__":

    multiplicando = float(input("Multiplicando: "))
    multiplicador = float(input("Multiplicador: "))
    resultado = multiplicacion(multiplicando, multiplicador)
    print(f"{multiplicando} * {multiplicador} = {resultado}")
