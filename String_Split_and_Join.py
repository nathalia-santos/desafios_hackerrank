def split_and_join(line):
    if ' ' in line:
        line = line.split(" ")
        print(line)
        line = "-".join(line)
    return line

line = 'this is a string'
result = split_and_join(line)
print(result)