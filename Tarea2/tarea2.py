def Multiplos(n):
    a=0
    for i in range(1,n):
        if n%i==0:
            a+=i
    return a
def NumAmigo(n):
    fin=0
    contador=1
    numeros_finales=[]
    while fin<n:
        nuamigo1=Multiplos(contador)
        nuamigo2=Multiplos(nuamigo1)
        if contador==nuamigo2 and contador==nuamigo1:
            contador+=1
        if contador==nuamigo2 and contador!=nuamigo1:
            numeros_finales.append(contador)
            fin+=1
            contador+=1
        else:
            contador+=1
    return numeros_finales