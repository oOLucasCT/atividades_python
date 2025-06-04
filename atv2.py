# Pede uma temperatura em Celsius ao usuário e converta-a para Fahrenheit utilizando a fórmula:
# Fahrenheit = (Celsius * 9/5) + 32


graus = int(input("digite a temperatura em celsius "))

result = (graus * 9/5) + 32

print(f"a temperatura em graus Fahrenheit é {result:.2f}")
