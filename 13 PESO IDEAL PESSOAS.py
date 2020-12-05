print('13ºTendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:')

print('Peso ideal para HOMENS')

a = float(input('Digite a sua altura,(Exemplo: 1.70):'))
pi = (72.7 * a) - 58
print(' Seu peso ideal é: {:.1f}kg.'.format(pi))

print(75*'-')

print('Peso ideal para MULHERES')
a = float(input('Digite a sua altura,(Exemplo: 1.65):'))
pi = (62.1 * a) - 44.7
print('Seu peso ideal é: {:.1f}kg.'.format(pi))