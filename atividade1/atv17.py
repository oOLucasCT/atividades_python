# Solicita o usuário o salário bruto e demonstra qunato sera o salário líquido (com base na contribuição INSS de 2023)

salario = float(input("digite seu salário de contribuição no INSS: "))

if salario <= 1692.72:
   contribuicao = salario * 0.08
   print ("Alíquota para recolhimento = 8%")

elif 1692.73 <= salario <= 2822.90:
   contribuicao = salario * 0.09
   print ("Alíquota para recolhimento = 9%")

else:
   contribuicao = salario * 0.08
   print ("Alíquota para recolhimento = 11%")

liquido = salario - contribuicao

print(f"Contribuição do INSS: R${contribuicao:.2f}")
print(f"Salário líquido: R$ {liquido}")