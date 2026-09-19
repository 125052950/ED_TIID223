""" #Declarando un arreglo 
numeros = [10, 20, 30, 40, 50]

#Imprimir la p. 30
print(numeros[2])

#Reasigne el valor de la p. 3 a 15
numeros[3] = 15
print(numeros)

#Agregamos un valor al final del arreglo
numeros.append(60)
print(numeros)

#Eliminamos por pos.
numeros.pop(1)
print(numeros)

#Eliminamos por valor
numeros.remove(30)
print(numeros) """

frutas = ["Mango", "Manzana", "Uva", "Pera", "Maracuya"]
frutas.remove("Uva")
print(frutas)

frutas.pop(3)
print(frutas)

frutas.append("Kiwi")
print(frutas)

frutas[2] = "Fresa"
print(frutas)

arreglo=[]
n = int(input("Ingrese el tamaño del arreglo: "))
n1 = int(input("Ingrese el valor 0: "))
arreglo.append(n1)
print(arreglo)