lista1=["Tilin",30,8.7,True,"Insano",30.7]
print(lista1)
print(lista1[0])
print(lista1[:])
print(lista1[2])
print(lista1[-1])
print(lista1[0:3])
print(lista1[:3])


lista1.append("HolaTilin")
print(lista1)


lista1.insert(2,"Paulo")
print(lista1)

lista1.extend(['dos',1.1,False])
print(lista1)



lista1.remove(30)
print(lista1)

lista1.pop()
print(lista1)

lista2=['tres,cuatro,cinco,seis']
lista3=lista1+lista2
print(lista3)

print(lista2*4)
lista4=[2,1,5,4,3]
print(lista4)
lista4.sort()
print(lista4)
lista4.reverse()
print(lista4)