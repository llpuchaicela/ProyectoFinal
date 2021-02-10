#Función para crear un vector 

def DefinirTamano(A):
    for i in range(10):
        valor=int(input(f'A {i} : '))
        A.append(valor)
    return A

def Imprimir(A):
    print(" Los elementos del vector son  : " )
    for i in range(len(A)):
        print(A[i], ", " , end= " ") 
        
def IngresarDigito():
    print(" ")
    dig=int(input("Ingrese el digito a verificar  "))
    return dig

def Respuesta(A, dig):
    aux=[0 for i in range (10)]
    conta=0
    for i in  range (10):
        if((A[i] > 100 )and( A[i] < 1000000000)):
            aux[i]=  (A[i])/10
        if((int(aux[i] % 10)) == dig):
            conta= conta+1;
            print(A[i], ", " , end= " ")
    print("")    
    return conta
#Metodo Principal
A=[]
A=DefinirTamano(A)
Imprimir(A)
dig=IngresarDigito()
print("El numero a buscar como penultimo en cada vector  es :  " ,dig)
res=Respuesta(A,dig)
print("La cantidad de números del vector en donde dicho dígito está de penúltimo es : " , res )









