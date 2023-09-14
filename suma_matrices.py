#Este script suma 2 matrices normales y NUMPY

A=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

B=[
    [9,8,7],
    [6,5,4],
    [3,2,1]
]

C=[]

for k in range(3):
    for i in range(3):
        sumaMatriz=A[k][i]+B[k][i]
        print(sumaMatriz)

#Fila primero y columna 

for i in range(3):
        sumaMatriz=A[0][i]+B[0][i]
        print(sumaMatriz)

for i in range(3):
        sumaMatriz=A[1][i]+B[1][i]
        print(sumaMatriz)

for i in range(3):
        sumaMatriz=A[2][i]+B[2][i]
        print(sumaMatriz)
   


for i in range(len(A)):
    # Inicializar una lista vacía para la fila actual de C
    suma = []
    # Iterar a través de las columnas de A y B
    for j in range(len(A[0])):
        # Sumar los elementos correspondientes de A y B y agregarlos a la fila de C
        suma.append(A[i][j] + B[i][j])
    # Agregar la fila a la matriz resultante C
    C.append(suma)

# Imprimir la matriz resultante C
for suma in C:
    print(suma)

