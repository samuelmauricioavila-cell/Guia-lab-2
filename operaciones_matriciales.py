class OperacionesMatriciales:
    def __init__(self, matriz_a=None, matriz_b=None, vector=None):
        self.matriz_a = matriz_a
        self.matriz_b = matriz_b
        self.vector = vector
        self._resultado_suma = None
        self._resultado_producto = None
        self._resultado_mat_vec = None
        self._resultado_inversa = None
    def sumar_matrices(self):
        if not self.matriz_a or not self.matriz_b:
            self._resultado_suma = "Error: Matrices vacías."
            return
        filas_a = len(self.matriz_a)
        columnas_a = len(self.matriz_a[0])
        filas_b = len(self.matriz_b)
        columnas_b = len(self.matriz_b[0])
        if filas_a != filas_b or columnas_a != columnas_b:
            self._resultado_suma = "Error: Las dimensiones de las matrices deben ser idénticas para sumarlas."
            return
        matriz_res = [[0.0 for _ in range(columnas_a)] for _ in range(filas_a)]
        for i in range(filas_a):
            for j in range(columnas_a):
                matriz_res[i][j] = self.matriz_a[i][j] + self.matriz_b[i][j]
        self._resultado_suma = matriz_res
    def multiplicar_matrices(self):
        filas_a = len(self.matriz_a)
        cols_a = len(self.matriz_a[0])
        cols_b = len(self.matriz_b[0])
        matriz_res = [[0.0 for _ in range(cols_b)] for _ in range(filas_a)]
        for i in range(filas_a):
            for j in range(cols_b):
                suma = 0.0
                for k in range(cols_a):
                    suma += self.matriz_a[i][k] * self.matriz_b[k][j]
                matriz_res[i][j] = suma
        self._resultado_producto = matriz_res
    def multiplicar_por_vector(self):
        filas = len(self.matriz_a)
        cols = len(self.matriz_a[0])
        vector_res = [0.0 for _ in range(filas)]
        for i in range(filas):
            suma = 0.0
            for j in range(cols):
                suma += self.matriz_a[i][j] * self.vector[j]
            vector_res[i] = suma
        self._resultado_mat_vec = vector_res
    def calcular_inversa(self):
        n = len(self.matriz_a)
        aumentada = []
        for i in range(n):
            fila = [float(x) for x in self.matriz_a[i]]
            identidad = [1.0 if i == j else 0.0 for j in range(n)]
            aumentada.append(fila + identidad)
        for i in range(n):
            pivote = aumentada[i][i]
            if abs(pivote) < 1e-12:
                swapped = False
                for k in range(i + 1, n):
                    if abs(aumentada[k][i]) > 1e-12:
                        aumentada[i], aumentada[k] = aumentada[k], aumentada[i]
                        pivote = aumentada[i][i]
                        swapped = True
                        break
                if not swapped:
                    self._resultado_inversa = "Error: La matriz es singular (no tiene inversa)."
                    return
            for j in range(2 * n):
                aumentada[i][j] /= pivote
            for k in range(n):
                if k != i:
                    factor = aumentada[k][i]
                    for j in range(2 * n):
                        aumentada[k][j] -= factor * aumentada[i][j]     
        inversa = [aumentada[i][n:] for i in range(n)]
        self._resultado_inversa = inversa
    def get_resultado_suma(self):
        return self._resultado_suma
    def get_resultado_producto(self):
        return self._resultado_producto
    def get_resultado_mat_vec(self):
        return self._resultado_mat_vec
    def get_resultado_inversa(self):
        return self._resultado_inversa