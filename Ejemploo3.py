
def calcular_area_triangulo(base, altura):

    return 0.5 * base * altura

def solicitar_entrada(mensaje):

    try:
        valor = float(input(mensaje))
        return valor
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        return solicitar_entrada(mensaje)

def main():

    print("\nCálculo del área del triángulo:")
    base_triangulo = solicitar_entrada("Ingrese la base del triángulo: ")
    altura_triangulo = solicitar_entrada("Ingrese la altura del triángulo: ")
    area_triangulo = calcular_area_triangulo(base_triangulo, altura_triangulo)
    print("Área del triángulo:", area_triangulo)

if __name__ == "__main__":
    main()
