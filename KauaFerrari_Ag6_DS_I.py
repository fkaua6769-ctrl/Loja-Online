valor_compra = float(input("Digite o valor total da compra: "))
#Solicita o valor total da compra

if valor_compra < 200:
    desconto_5 = valor_compra * 0.05
    print(f"Você recebeu um desconto de 5%, sendo: R${desconto_5:.2f}!")
    print(f"O valor final da compra é: R${valor_compra - desconto_5:.2f}")
#A compra com valor menor que 200 reais recebe um desconto de 5%

if valor_compra >= 200 and valor_compra < 300:
    desconto_10 = valor_compra * 0.10
    print(f"Você recebeu um desconto de 10%, sendo: R${desconto_10:.2f}!")
    print(f"O valor final da compra é: R${valor_compra - desconto_10:.2f}")
#A compra com valor menor ou igual a 200 reais e menor que 300 reais recebe um desconto de 10%

if valor_compra >= 300:
    desconto_15 = valor_compra * 0.15
    print(f"Você recebeu um desconto de 15%, sendo: R${desconto_15:.2f}!")
    print(f"O valor final da compra é: R${valor_compra - desconto_15:.2f}")
#A compra com valor maior ou igual a 300 reais recebe um desconto de 15%