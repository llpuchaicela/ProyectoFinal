A= []
B = []

# Matriz A
print ("La matriz A es : ")
for i in range(4):
    A.append([])
    for j in range(6):
        x=int(input('Ingresa el elementos de (%d,%d):' % (i, j)))
        A[i].append(x)
for i in range(4):
    print(A[i])

# Matriz B
print ("La matriz B es : ")
for i in range(4):
    B.append([])
    for j in range(6):
        y= int(input('Ingresa el elementos de (%d,%d) :' % (i, j)))
        B[i].append(y)
for i in range(4):
    print(B[i])

SA = (A[0][0] + A[3][0] + A[0][5] + A[3][5]);
promA = float(SA/4)     

SB = (B[0][0] + B[3][0] + B[0][5] + B[3][5]);
promB = float(SB/4)     
print("La suma de las esquinas de la matriz A es : " , SA)
print("La suma de las esquinas de la matriz B es : " , SB)
print("El promedio de la matriz A es: ", promA)
print("El promedio de la matriz B es: ", promB)  

if(promA==promB):
    print("El promedio de las esquinas de las matrices son iguales")
else:
    print
    print("Sus promedios son diferentes ")   