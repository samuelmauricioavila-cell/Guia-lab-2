class OrdenamientoListas:
    def __init__(self, lista=None):
        self.lista_original = lista if lista is not None else []
        self._res_burbuja = None
        self._res_insercion = None
        self._res_seleccion = None
        self._res_mergesort = None
        self._res_python_sort = None
    def ordenar_burbuja(self):
        A = list(self.lista_original)
        n = len(A)
        for j in range(n):
            for i in range(0, n - j - 1):
                if A[i] > A[i + 1]:
                    A[i], A[i + 1] = A[i + 1], A[i]
        self._res_burbuja = A
    def ordenar_insercion(self):
        A = list(self.lista_original)
        for j in range(1, len(A)):
            key = A[j]
            i = j - 1
            while i >= 0 and A[i] > key:
                A[i + 1] = A[i]
                i -= 1
            A[i + 1] = key
        self._res_insercion = A
    def ordenar_seleccion(self):
        A = list(self.lista_original)
        n = len(A)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if A[j] < A[min_idx]:
                    min_idx = j
            A[i], A[min_idx] = A[min_idx], A[i]
        self._res_seleccion = A
    def ordenar_mergesort(self):
        def merge_sort_rec(arr):
            if len(arr) > 1:
                mid = len(arr) // 2
                L = arr[:mid]
                R = arr[mid:]
                merge_sort_rec(L)
                merge_sort_rec(R)
                i = j = k = 0
                while i < len(L) and j < len(R):
                    if L[i] <= R[j]:
                        arr[k] = L[i]
                        i += 1
                    else:
                        arr[k] = R[j]
                        j += 1
                    k += 1
                while i < len(L):
                    arr[k] = L[i]
                    i += 1
                    k += 1
                while j < len(R):
                    arr[k] = R[j]
                    j += 1
                    k += 1
            return arr
        A = list(self.lista_original)
        self._res_mergesort = merge_sort_rec(A)
    def ordenar_python_sort(self):
        A = list(self.lista_original)
        A.sort()
        self._res_python_sort = A
    def get_resultado_burbuja(self):
        return self._res_burbuja
    def get_resultado_insercion(self):
        return self._res_insercion
    def get_resultado_seleccion(self):
        return self._res_seleccion
    def get_resultado_mergesort(self):
        return self._res_mergesort
    def get_resultado_python_sort(self):
        return self._res_python_sort