a = int(input('Ingrese cuantos numeros perfectos quiere ver: '))
def Multiplos(n):
    a=0
    for i in range(1,n):
        if n%i==0:
            a+=i
    return a
def NumPerfecto(n):
    contador=0
    numero=['primer','segundo','tercer','cuarto','quinto']
    numeros=[]
    for i in range(1,10**n):
        a=Multiplos(i)
        if a==i:
            numeros.append(a)
            print("El: "+str(numeros[contador])+ " es el " +str(numero[contador]) + " numero perfecto")
            contador+=1
    return numeros
NumPerfecto(a)