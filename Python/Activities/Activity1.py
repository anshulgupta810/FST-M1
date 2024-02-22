name = input('Please enter your name')
age = int(input('Please enter your age'))
print(name,age)

year = ( 2023 - age ) + 100

print(name + " will be 100 years old in the year " + str(year))


def total(initial = 5, *num, **key):
    print('>>>>>initial  ',str(initial))
    count = initial
    print('>> ',count)
    for n in num:
        print('> ',n,' in ',)
        count+=n
        print('> count ',count)
        for k in key:
            print(' keys ',key)
            print('from  for ',k)
            print('from  for ',count)
            count+=key[k]
            print('>>> ',count)
            return count
print(total(100,2,3, clouds=50, stars=100))

print(2**2)
print(2**2**3)
print(2**2**3**1)

list = ['a', 'b', 'c']
list+= 'de'
print(list)