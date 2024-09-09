# Función para calcular el área de un rectángulo
def f(a, b):
    result = a * b
    return result

# Función para calcular el área de un triángulo
def g(b, h):
    r = 0.5 * b * h
    return r

# Función principal
def main():
    x = 4
    y = 6
    rect_area = f(x, y)
    print("Área del rectángulo:", rect_area)

    base = 5
    altura = 8
    tri_area = g(base, altura)
    print("Área del triángulo:", tri_area)

main()
