n = int(input().strip())
#Se n é estranho, imprima Weird
#Se n é par e na faixa inclusiva de 2 para 5, imprimir Not Weird
#Se n é par e na faixa inclusiva de 6 para 20, imprimir Weird
#Se n é par e maior que 20, imprimir Not Weird

if n % 2 == 0 and n >= 2 and n <= 5:
    print('Not Weird')
elif n % 2 == 0 and n >= 6 and n <= 20:
    print('Weird')
elif n % 2 == 0 and n > 20:
    print('Not Weird')
else:
    print('Weird')