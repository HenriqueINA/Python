lista = []
for i in range(1,11):
    lista.append(i)
print(lista)

#print da lista de 1 a 10
listac = [i for i in range (1,11)]   
print(listac)

#print do dobro da lista
dobro = [i*2 for i in lista]
print(dobro)

#print da lista apartir do numero 5
maior_que_6 = [i for i in lista if i > 5]
print(maior_que_6)

for i in lista:
    if i > 5:
        maior_que_6.append(i)

#print multiplos de 3        
multiplos_de_3 = [i*2 if i % 3 == 0 else i for i in lista]
print(multiplos_de_3)

multiplos_de_3_filtrados_pares = \
[i*2 if i % 3 == 0 else i for i in lista if i % 2 == 0]
print(multiplos_de_3_filtrados_pares)            