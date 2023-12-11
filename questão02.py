#peça ao usuario para digitar seu salario
b = float(input("digite seu salario: "))

#se seu salário foi igual ou menor ou igual a 400, vc terá um aumento de 15%
if b <= 400.00:
    print("Aumento percentual de 15%")
    a = b * 15 / 100
    print(f"Seu aumento foi de: {a}")
    print(f"Seu novo salário é: {a+b}")

#se seu salário for menor ou igual a 800, vc terá um aumento de 12%
elif b <= 800.00:
    print("Aumento percentual de 12%")
    a = b * 12 / 100
    print(f"Seu aumento foi de: {a}")
    print(f"Seu novo salário é: {a+b}")

#se seu salário for menor ou igual a 1200, vc terá um aumento de 10%
elif b <= 1200.00:
    print("Aumento percentual de 10%")
    a = b * 10 / 100
    print(f"Seu aumento foi de: {a}")
    print(f"Seu novo salário é: {a+b}")

#se seu salário for menor ou igual a 2000, vc terá um aumento de 7%
elif b <= 2000.00:
    print("Aumento percentual de 7%")
    a = b * 7 / 100
    print(f"Seu aumento foi de: {a}")
    print(f"Seu novo salário é: {a+b}")

#se seu salário for maior que 2000, vc terá um aumento de 4%
else:
    print("Aumento percentual de 4%")
    a = b * 4 / 100
    print(f"Seu aumento foi de: {a}")
    print(f"Seu novo salário é: {a+b}")