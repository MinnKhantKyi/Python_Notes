ls = [10,3,45,8,15]
found = False
index = 0

data = int(input('Plz enter a number > '))

while index < len(ls):
    if ls[index] == data:
        found = True
        break
    index +=1

if not found:
    print('No match data in List.')
    ls.append(data)
    print('Data in the List > {}'.format(ls))
else:
    print('Found match data in the List')
    print('Data in the List > {}'.format(ls))