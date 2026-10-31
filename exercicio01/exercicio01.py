print ("Olá, Mundo!")

letra = input("Digite uma letra: ")
if letra == "a":
    print ("Valido!")
else:
    print ("Invalido!")

idade = int(input("Digite sua idade: "))
if idade >= 18:
    print ("Maior de idade!")
else:
    print("Menor de idade!")

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
soma = n1 + n2
print(f'a soma dos dois valores é {soma}')
