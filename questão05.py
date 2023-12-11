#coloque um valor na variavel que ira guardar os numeros pares
np = 0
#crie um loop para ler 5 numeros
for i in range(5):
    #peça ao usuario para digitar 5 numeros
    valor = int(input(f"Digite o {i + 1} número: "))
    #verificar se o numero digitado é par
    if valor % 2 == 0:
        np += 1
#exibir o resultado com "PRINT"
print(f"\n valores pares: {np}")