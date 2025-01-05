carros = ['Marea','Fusca','Chevette']
print(carros)

# Formas de adcionar elementos na lista

carros.append('Corcel')
print(carros)

print(carros[2])

carros.insert(1,'Escort')
print(carros)

#Formas de remover elementos da lista

carros.pop()
print(carros)

del carros[1]
print(carros)

carros.remove('Chevette')
print(carros)

# count - retorna a quantidade de elementos iguais na lista
carros.append('Fusca')

print(carros.count('Fusca'))

carros.pop()
carros.append('Kombi')
print(carros)

#ordenador alfa numerico
carros.sort()
print(carros)

# inverter uma lista
carros.reverse()
print(carros)