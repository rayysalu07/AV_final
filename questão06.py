#criar uma lista de "n" e da variável "p"
n = []
p = 0
#crie um loop para repetir 6 vezes
for i in range(0,6):
#peça ao usuario para digitar um numero
    num = float(input(f"Digite o {i+1} número: "))
#se o número for maior que 0, adicionar 1 na variável positivo,
#colocar ele na lista "n"
    if num>0:
        p = p+1
        n.append(num)
#somar todos os números da lista "n"
soma = sum(n)
#mostrar a quantidade de valores positivos com o "PRINT"
print(f"existem {p} valores positivos")
#criar um bloco onde apenas numeros positivos terao sua media calculada
if num != -0:
    #mostrar a média da lista "n" com o "PRINT"
    print(f"a media dos valores é: {soma/p}")