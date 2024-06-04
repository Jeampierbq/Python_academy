#Listas en Python
#Definir una lista de tipo str
nombres = ['Jeampier','Ana','Anderson','Valeria']
#Imprimir la lista
print(nombres)
#Para acceder a los elementos de un a lista
print(nombres[0])
#Para acceder a los elementos de manera inversa
print(nombres[-1])
#Para imprimir un rango
print(nombres[0:2])
#Ir del inicio de la lista al indice (sin incluirlo)
print(nombres [ : 3])
#Para cambiar un valor
nombres[3]= 'Daniela'
print(nombres)
#Para iterar una lista
for nombre in nombres :
     print(nombre)
else:
    print('Los unicos nombres')
#Para preguntar
print(len(nombres))
#Agregar un elemento
nombres.append('Barbara')
print(nombres)
#Insertar un elemento a un indice en especifico
nombres.insert(2,'Kimberly')
print(nombres)
#Remover un elemento
nombres.remove('Kimberly')
print(nombres)
#Remover el ultimo valor agregado
nombres.pop()
print(nombres)
