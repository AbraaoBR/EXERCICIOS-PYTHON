print('15ºFaça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:')
ganho = float(input('Quanto você ganha por hora? R$'))
horas = float(input('Quantas horas você trabalhou no mês?'))

salario = (ganho * horas)
ir = (11 * salario / 100)
inss = (8 * salario / 100)
sindicato = (5 * salario / 100)

print('O seu salário bruto foi de R${}.'.format(salario))
print('Você pagou de imposto de renda a receita federal: R${:.2f}'.format(ir))
print('Você pagou de imposto ao INSS: R${:.2f}'.format(inss))
print('Você pagou de imposto ao Sindicato: R${:.2f}'.format(sindicato))
print('Seu salário liquido é de R${:.2f}'.format(salario - ir - inss - sindicato))
