import numpy as np

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Python")
    
    # Lambda expression
    # 1)
    # Realizar una funcion lambda que eleve al cuadrado
    # el número pasado como parámetro
    cuadrado = lambda x: x**2
    print("El cuadrado del número 5 es:", cuadrado(5))

    # 2)
    # Utilice la función map para mapear una lambda expression
    # que retorne la potencia de 2 de cada numero en la lista numeros
    # El resultado (la potencia de cada numero) se debe ir almacenando
    # en una nueva lista
    numeros = [1, -5, 4, 3]
    print("La lista inicial es:", numeros)
    numeros_potencia = list(map(lambda x: x**2, numeros))
    print("La lista de potencias al cuadrado, según la lista inicial es:", numeros_potencia)


    # Nota: realizar la lambda expression "in line", es decir,
    # no declarar la lambda fuera del map sino diretamente dentro
    # Copiar la lambda creada en el paso anterior dentro del map
    # NOTA: No debe usar "potencia_2" dentro del map, debe colocar
    # directamente la lambda.

    print("Ejercicio 1 - Finalizado")