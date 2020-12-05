print('17ºFaça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de '
      'Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).')

print(75*'=')
tamanho = int(input('Digite o tamanho do arquivo em MB:'))
velocidade = int(input('Digite a velocidade da internet em Mbps:'))
tempo = int(tamanho / velocidade * 7.5)
minutos = int(tempo / 60)
segundos = int(tempo % 60)
print('Download será completado em {:.0f}min e {:.0f}s'.format(minutos, segundos))
