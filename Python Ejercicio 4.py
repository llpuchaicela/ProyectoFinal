#Ejercicio 4
M = [[0 for j in range(0,7)]for i in range (0,7)]

print("Matriz espiral")
n= int(input("Ingrese limite de matriz  " ))

x=int(( n-1)/2)
y=int((n-1)/2)
i=x
serie=1
de=0
impar=1
#Ingresar datos a la matriz
while (serie<= n*n):
    for j in range (y,y+1):
        M[i][j]=serie
        serie=serie+1
        l=j
        
    for i in range (x-de, (x-1)-impar, -1):
        j=l+1
        M[i][j-de]= serie
        serie=serie+1
        y=j-de
        k=i

    for j in range (y-1, (k-1),-1):
        i=k
        M[i][j]= serie
        serie=serie+1
        l=j
        
    for i in range (l+1, x+2):
        j=l
        M[i][j]= serie
        serie=serie+1
        y=j
        k=i
        
    for j in range (y+1, i+1):
        i=k
        M[i][j]= serie
        serie=serie+1
        l=j
        
    y=l+1
    x=k
    impar = impar+2
    de=1
    
for i in range (n):
    for j in range (n):
        if (M[i][j]<10):
            print("" ,M[i][j] ,end = "  ")
        else:
            print(M[i][j] ,end = "  ")
    print("")