#!/usr/bin/python3
# shebang
# print('Questionário\n')
# nome = input("Qual é o time do coração do Pedro?  ")
# if nome == "todos":
#     print("Você acertou! :-D\n")
# else:
#     print("Você errou! :-(\n")

frutas = ['abacaxi']
print(frutas)
frutas.append('laranja')
frutas.append('limão')
print(frutas)
print(frutas[1])
print(frutas)
frutas.pop(2)
print(frutas)

aleatorios = [1, 500, [1,2,3],'cachorro', True, False, 1.8, 111]

frutas.insert(1, 'melancia')
print(frutas)
frutas.remove('abacaxi')
print(frutas)
print(aleatorios[2][2])

print(500 in aleatorios)

#frutas.sort(reverse=True)
frutas.reverse()

print(frutas)


#print(aleatorios.reverse()

books = {
   "eBooks":[
      {
         "language":"Pascal",
         "edition":"third",
         "value": 7.40
      },
      {
         "language":"Python",
         "edition":"four"
      },
      {
         "language":"SQL",
         "edition":"second"
      }
   ]
}

print(books)




dados = {

    'cidades': {
        'saopaulo': {
            'nome': 'São Paulo',
            'municipios': 645,
            'população': 12.18
        },
        'riodejaneiro': {
            'nome': 'Rio de Janeiro',
            'municipios': 92,
            'população': 6.32
        },
        'minasgerais': {
            'nome': 'Minas Gerais',
            'municipios': 31,
            'população': 20.87

        }
    }
}


# imprima a quantiddade de municipios de minas
print(dados['cidades']['minasgerais']['municipios'])
# imprima a quantidade de municipios do rio

# imprima o nome e população de são paulo em milhoes

# imprima a quantiddade de municipios de minas

# imprima a quantidade de municipios do rio

# imprima o nome e população de são paulo em milhoes




# ['rafaela','luis', 'joao', 'ana', 'paulo', 'fernando', 'marilia', 'tarcisio', 'carlos', 'manuel']

lista = ['rafaela','luis', 'joao', 'ana', 'paulo', 'fernando', 'marilia', 'tarcisio', 'carlos', 'manuel']
for l in lista:
    print(f'seja bem-vindo(a) {l}')




# faça um for que imprima o nome de cada pessoa da lista e com a mensagem 'bem-vindo {}'