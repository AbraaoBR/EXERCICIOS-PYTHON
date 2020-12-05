print('12ºTendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58')
a = float(input('Digite a sua altura,(Exemplo: 1.74):'))
pi = (72.7 * a) - 58
print('Seu peso ideial é: {:.1f}kg'.format(pi))