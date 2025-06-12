# Solicitando ao usuário um valor principal, a taxa de juros (em porcentagem) e o número de anos
# Montante = principal + (principal * taxa de juros * anos / 100)

valor = float(input("Valor principal: "))

taxa = float(input("Taxa de juros: "))

anos = int(input("Números de anos: "))

montante = valor + (valor * taxa * anos / 100)

print(f"O valor montante é {montante:.2f}")
