n = 6
debts = [['Alex', 'Blake', '5'], ['Blake', 'Alex' ,'3'], ['Casey', 'Alex', '7'], ['Casey', 'Alex', '4'],
['Casey', 'Alex', '2']]

v_alex = 0
v_blake = 0
v_casey = 0
maior_devedor = []
maior_valor_devido = 0
lista_devedores = []
devedores = {}
for i in range(len(debts)):
    if debts[i][0] == 'Alex':
        v_alex -= int(debts[i][2])
    elif debts[i][0] == 'Blake':
        v_blake -= int(debts[i][2])
    elif debts[i][0] == 'Casey':
        v_casey -= int(debts[i][2])
for i in range(len(debts)):
    if debts[i][1] == 'Alex':
        v_alex += int(debts[i][2])
    elif debts[i][1] == 'Blake':
        v_blake += int(debts[i][2])
    elif debts[i][1] == 'Casey':
        v_casey += int(debts[i][2])

if v_alex < 0 and v_alex <= v_blake and v_alex <= v_casey:
    maior_devedor.append('Alex')
elif v_blake < 0 and v_blake <= v_alex and v_blake <= v_casey:
    maior_devedor.append('Blake')
elif v_casey < 0 and v_casey <= v_alex and v_casey <= v_blake:
    maior_devedor.append('Casey')

    

print(v_alex)
print(v_blake)
print(v_casey)
print(maior_devedor)

