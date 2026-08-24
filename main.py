import random
from operaciones_matriciales import OperacionesMatriciales
from ordenamiento import OrdenamientoListas
def leer_matriz(nombre):
    print(f"\n--- Ingrese la {nombre} ---")
    filas = int(input("Número de filas: "))
    cols = int(input("Número de columnas: "))
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(cols):
            val = float(input(f"Elemento [{i}][{j}]: "))
            fila.append(val)
        matriz.append(fila)
    return matriz
def leer_vector(tam):
    print(f"\n--- Ingrese el vector de tamaño {tam} ---")
    vector = []
    for i in range(tam):
        val = float(input(f"Elemento [{i}]: "))
        vector.append(val)
    return vector
def menu_punto_3_1():
    while True:
        print("\n*** SUBMENÚ: OPERACIONES MATRICIALES ***")
        print("1. Suma de matrices")
        print("2. Producto de matrices")
        print("3. Producto de matriz por vector")
        print("4. Inversa de una matriz")
        print("5. Regresar al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            print("\nNota: Las matrices deben ser de las mismas dimensiones.")
            mat_a = leer_matriz("Matriz A")
            mat_b = leer_matriz("Matriz B")
            op = OperacionesMatriciales(matriz_a=mat_a, matriz_b=mat_b)
            op.sumar_matrices()
            res = op.get_resultado_suma()
            print("\nResultado Suma:")
            if isinstance(res, str):
                print(res)
            else:
                for fila in res:
                    print(fila)
        elif opcion == '2':
            print("\nNota: Columnas de A deben ser iguales a filas de B.")
            mat_a = leer_matriz("Matriz A")
            mat_b = leer_matriz("Matriz B")
            op = OperacionesMatriciales(matriz_a=mat_a, matriz_b=mat_b)
            op.multiplicar_matrices()
            print("\nResultado Producto de Matrices:")
            for fila in op.get_resultado_producto():
                print(fila)
        elif opcion == '3':
            mat_a = leer_matriz("Matriz A")
            cols_a = len(mat_a[0])
            vector = leer_vector(cols_a)
            op = OperacionesMatriciales(matriz_a=mat_a, vector=vector)
            op.multiplicar_por_vector()
            print("\nResultado Producto Matriz x Vector:", op.get_resultado_mat_vec())
        elif opcion == '4':
            print("\nNota: La matriz debe ser cuadrada.")
            mat_a = leer_matriz("Matriz Cuadrada")
            if len(mat_a) != len(mat_a[0]):
                print("Error: La matriz no es cuadrada.")
                continue
            op = OperacionesMatriciales(matriz_a=mat_a)
            op.calcular_inversa()
            res = op.get_resultado_inversa()
            print("\nResultado Inversa:")
            if isinstance(res, str):
                print(res)
            else:
                for fila in res:
                    print([round(x, 4) for x in fila])  
        elif opcion == '5':
            break
        else:
            print("Opción inválida, intente de nuevo.")
def menu_punto_3_2():
    while True:
        print("\n*** SUBMENÚ: ALGORITMOS DE ORDENAMIENTO ***")
        cantidad = int(input("Ingrese la cantidad de números flotantes aleatorios: "))
        lista_aleatoria = [round(random.uniform(-100, 100), 2) for _ in range(cantidad)]
        print(f"\nLista generada: {lista_aleatoria}")
        ord_obj = OrdenamientoListas(lista=lista_aleatoria)
        ord_obj.ordenar_burbuja()
        ord_obj.ordenar_insercion()
        ord_obj.ordenar_seleccion()
        ord_obj.ordenar_mergesort()
        ord_obj.ordenar_python_sort()
        print("\n--- RESULTADOS DE ORDENAMIENTO ---")
        print("1. Burbuja:     ", ord_obj.get_resultado_burbuja())
        print("2. Inserción:   ", ord_obj.get_resultado_insercion())
        print("3. Selección:   ", ord_obj.get_resultado_seleccion())
        print("4. Mergesort:   ", ord_obj.get_resultado_mergesort())
        print("5. Python Sort: ", ord_obj.get_resultado_python_sort())
        repetir = input("\n¿Desea generar otra lista y ordenar de nuevo? (s/n): ")
        if repetir.lower() != 's':
            break
def main():
    while True:
        print("\n========================================")
        print("   LABORATORIO 2 - PROGRAMACIÓN 3       ")
        print("========================================")
        print("1. Punto 3.1: Operaciones Matriciales")
        print("2. Punto 3.2: Algoritmos de Ordenamiento")
        print("3. Salir")
        opcion = input("Seleccione una opción principal: ")
        if opcion == '1':
            menu_punto_3_1()
        elif opcion == '2':
            menu_punto_3_2()
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
if __name__ == "__main__":
    main()