def maior_numero():
    num1= float(input('digite o 1° número:'))
    num2= float(input('digite o 2° número:'))
    num3= float(input('digite o 3° número:'))

    if num1 > num2 and num1> num3:
        print(f'O maior número é o {num1}')
    elif num2 > num1 and num2 >num3:
        print(f'O maior número é o {num2}')
    else:
        print(f'O maior número é o {num3}')

maior_numero()
