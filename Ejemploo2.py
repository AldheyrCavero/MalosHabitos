def calcular_suma_producto(multiplicador, sumando, aditivo):

    resultado_producto = multiplicador * sumando
    resultado_final = resultado_producto + aditivo
    return resultado_final


def solicitar_entrada(mensaje):

    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")


def ejecutar_calculo():

    multiplicador = solicitar_entrada("Ingrese el valor del multiplicador: ")
    sumando = solicitar_entrada("Ingrese el valor del sumando: ")
    aditivo = solicitar_entrada("Ingrese el valor del aditivo: ")

    resultado = calcular_suma_producto(multiplicador, sumando, aditivo)
    print("El resultado es:", resultado)


ejecutar_calculo()
