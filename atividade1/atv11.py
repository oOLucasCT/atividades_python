# Determinando o Triângulo 

# Solicitando os valores dos lado do Triângulo
print("Considerando os lados do triângulo sendo A, B e C. Determine o valor deles: ")
ladoA = int(input("Lado A do triângulo= "))
ladoB = int(input("Lado B do triângulo= "))
ladoC = int(input("Lado C do triângulo= "))

# Equilatero tem todos os lados iguais
if (ladoA == ladoB == ladoC) :
    print("Este é um triângulo EQUILÁTERO")

# Escaleno tem todos os lados diferentes
elif (ladoA != ladoB != ladoC):
    print("Este é um triângulo ESCALENO")

# Isósceles tem dois lados iguais e um diferente
else:
    print("Este é um triângulo ISÓSCELES")