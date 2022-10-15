entrada = '8HYPotheticall024y6wxz'

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z' ]

alfabeto_maiusculo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
'V', 'W', 'X', 'Y', 'Z']

numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
resultado = []

for n in numeros:
    if n not in entrada:
        resultado.append(n)
for letra in alfabeto:
    if letra not in entrada:
        resultado.append(letra)
resultado_absoluto = ''.join(map(str, resultado))
    

print(resultado_absoluto)
