from math import sqrt
aux = 0

print("Ejercicio1")

# Ingresar el limite de tamaño de vector
n = int(input("Ingrese el limite del vector  "))
A = []
# Ingresar elementos al vector
for i in range(0, n):
    A.append(int(input(f'Introduce el elemento A {i} : ')))

# Presentar los elementos del vector

print("Los elementos del vector son")
for i in range(0, n):
    print(A[i])

# Verificar los digitos e imprimir cada digito con cada numero comprendido entre 1 y su digito
print("Los digitos de cada elemento del vector son : ")
print("  ")
for i in range(0, n):
    print(" ")
    print("***"  , A[i] , "***")
    print(" ")
    number = A[i]
    
    while number > 0:
        rest = number % 10  # 5.6
        aux = (aux * 10)+rest  # 5.6
        number = int(number/10)
    A[i] = aux
    while (A[i] != 0): 
        digito =int(A[i] % 10)
        aux = 0
        print("-- ", digito, " -- ")
        print(" ")
        for j in range(1, digito+1):
            print(j, ", " , end= "" )
        print("")
        A[i] = int(A[i] / 10)
      
        