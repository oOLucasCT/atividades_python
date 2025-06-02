# Um programa que pergunte ao usuário o valor do café (um número), pergunte para ele quantos
# cafés ele irá querer comprar e apresente o resultado a pagar

valor_cafe = float(input("Digite o valor do café: R$"))

quant = int(input("Digite quantos cafés vai querer: "))

preco = valor_cafe * quant

print(f"Você terá de pagar R${preco:.2f}")