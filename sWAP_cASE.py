s = 'HackerRank.com presents "Pythonist 2"'

def swap_case(s):
    #outra forma de resolver:
    #return ''.join([i.lower() if i.isupper() else i.upper() for i in s])
    #outra forma de resolver:
    #return st.swapcase()
    new_s = ''
    for i in s:
        if i.isupper() == True:
            i = i.lower()
            new_s = new_s + i
        elif i.islower() == True:
            i = i.upper()
            new_s = new_s + i
        else:
            new_s = new_s + i
    s = new_s
    return s 

result = swap_case(s)
print(result)