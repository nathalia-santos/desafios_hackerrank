string = 'AbBaAbBaAbBa'
sub_string = 'Ab'

#iguais = set(s) & set(sub_string)
#print(iguais)

#print(len(iguais))
lista1 = []
lista2 = []
cont = 0

# for i in range(0, len(s)):
#     lista1.append(s[i])
# for i in range(0, len(sub_string)):
#     lista2.append(sub_string[i])

def count_substring(string, sub_string):
    count, last_index = 0,-1 
    for i in range(len(string)):
        if sub_string in string[i:]:
            if string[i:].index(sub_string) != last_index:
                count += 1
                last_index = string[i:].index(sub_string)
        last_index -= 1
    return count

print(count_substring(string, sub_string))
print(string[1:])