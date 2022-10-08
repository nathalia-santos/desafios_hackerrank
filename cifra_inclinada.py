def substitui(car, chave):
    return chr(ord(car)+chave)


def descodifica(encodedString,chave):
    descodificada =''
    for car in encodedString:
        descodificada = descodificada + substitui(car,+chave)
    return descodificada


print(descodifica('hello_world', 2))