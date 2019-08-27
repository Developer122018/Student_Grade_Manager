try:
    print('This is the text before the error')
    print('5'+5)
except NameError as n:
    print('This is the text after the name error ')
except TypeError as t:
    print('Type error')
    print(str(t))