import tarea2 as Amigos

a = int(input('Ingrese cuantos numeros perfectos quiere ver: '))
print("Las primeras "+ str(a)+ "parejas de numeros amigos son:\n")
amigo=Amigos.NumAmigo(2*a)
print(amigo)