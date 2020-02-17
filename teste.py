x = 1
y = 2

if x == y: 
    print("Numeros iguais")
elif y > x:
    print("Y é maior que X")
else:
    print("X é maior que Y")

lista = [1,2,3,4,5]
lista2 = ['ola','tudo','bem','?']

for i in lista:
    print('valor: {}'.format(i))

for i in lista2:
    print(i + ' ')

for i in range(0,80,2):
    print(i)

numero = input("Digite um numero: ")
print("numero digitado é {}".format(numero))
