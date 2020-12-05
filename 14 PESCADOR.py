print('14ºJoão Papo-de-Pescador')

print(75*'-')

peso = float(input('Digite quantos kg tem o peixe:'))

limite = 50
excesso = (peso - limite)
multa = (4 * excesso)

print('PEIXE COM {:.1f}kg'.format(peso))
print('O EXCESSO FOI DE: {:.1f}kg '.format(excesso))
print('A MULTA POR EXCESSO FOI DE: R${}'.format(multa))
