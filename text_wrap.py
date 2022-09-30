import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    result = wrapper.wrap(text=string)
    s = ""
    for i in result:
        s = s + i + "\n"
    return s

string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
max_width = int(input())
result = wrap(string, max_width)
print(result)
#ABCDEFGHIJKLIMNOQRSTUVWXYZ