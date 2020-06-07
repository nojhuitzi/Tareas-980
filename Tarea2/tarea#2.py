def Multiplos(n):
    a=0
    for i in range(1,n):
        if n%i==0:
            a+=i
    return a
def NumAmigo(n):
    i=0
    contador=1
    numeros=[]
    final=[]
    perfectos=[6,28,496,8128]
    while i<n:
        a=Multiplos(contador)
        b=Multiplos(a)
        if contador==b and contador==a:
            contador+=1
        if contador==b and contador!=a:
            numeros.append(contador)
            i+=1
            contador+=1
        else:
            contador+=1
    return numeros

a = int(input('Ingrese cuantos numeros perfectos quiere ver: '))
print(NumAmigo(2*a))