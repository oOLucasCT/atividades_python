# Pede ao usuário o valor de um produto e o percentual de desconto. 
# Calcule e mostre o valor com o desconto aplicado

valor = float(input("digite o valor do produto: R$"))
desconto = float(input("digite o desconto do produto: %"))

valor_final = valor - (desconto / 100)

print(f"O valor com desconto é de R${valor_final:.2}")