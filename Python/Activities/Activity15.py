x= input('enter name')

try:
    print(x)
except NameError:
    print("x hasn't been defined yet.")