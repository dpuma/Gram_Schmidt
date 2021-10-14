import numpy as np

def productoPunto(matrizA, matrizB):
    return np.dot(matrizA, matrizB)

def norma(Vec):
    return np.linalg.norm(Vec)

def proyeccion(Entrada, Salida, itera, actual):
    if (itera == actual):
        return
    Salida[actual] = Salida[actual] - (productoPunto(Entrada[actual], Salida[itera])/productoPunto(norma(Salida[itera]),norma(Salida[itera])))*Salida[itera];
    proyeccion(Entrada, Salida, itera + 1, actual)

def ortogonalizacion(Entrada):
    Salida = np.copy(Entrada)
    for i in range(0, len(Entrada)):
        proyeccion(Entrada, Salida, 0, i);
    return Salida

# main
Entrada = np.array([[1,1,1],[-1,0,-1],[-1,2,3]], dtype=float)
Salida = ortogonalizacion(Entrada)
np.set_printoptions(precision=5, suppress=True)

print("Matriz Entrada:\n", Entrada,"\n")
print("Matriz Ortogonal:\n", Salida)
