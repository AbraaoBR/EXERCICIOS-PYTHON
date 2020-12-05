print('9 e 10ºFaça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.')

print('CONVERSOR DE TEMPERATURAS')
print(75 * '_')

print('CELSIUS PARA FAHRENHEIT')
c = float(input('Digite a temperatura atual em ºC:'))
f = (c * 9 / 5) + 32
print('{}ºCelsius equivale a {:.1f}ºFahrenheit'.format(c, f))



print(75 * '_')
print('Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.')

print('FAHRENHEIT PARA CELSIUS')
f = float(input('Digite a temperatura atual em ºF:'))
c = float(5 * ((f - 32) / 9))
print('{}ºFahrenheit equivale a {:.1f}ºCelsius.'.format(f, c))
