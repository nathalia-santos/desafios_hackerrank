n = int(input())
phoneBook = {('sam', 99912222), ('tom', 11122222), ('harry', 12299933)}

for key, value in phoneBook:
    if n in phoneBook:
        print(f'{key}={value}')
    else:
        print('Not Found')