try:
    a = int('sdadsd')
except ValueError:
    print('ValueError!')
finally:
    print('Дошёл до finally')
