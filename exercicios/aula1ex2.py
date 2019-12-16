#!/usr/bin/python3
lista = ['Corinthians', [1, 2, 3, 4, 5] ,
         'Palmeiras', 'São Paulo', 
        [10, 11, 12, 13, 14],'Flamengo', 'Vasco']

print(lista)


# print 3, 13, Vasco
print(lista[1][2], lista[4][3], lista[6])
print(lista[1][2], lista[4][3], lista[-1])

# print 5, São Paulo, 14
print(lista[1][4], lista[3], lista[4][4])

# mude o valor de 4 para 40
lista[1][4] = 40
print(lista[1][4])

# mude o valor de 14 para 150
lista[4][4] = 150
print(lista[4][4])