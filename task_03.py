# 3. Сформировать из введенного числа обратное по порядку входящих 
# в него цифр и вывести на экран. Например, если введено число 
# 3486, то надо вывести число 6843.

print('Please enter an integer number')
n = int(input('>> '))
m = 0 
while n > 0:
    m = m * 10 + n % 10
    n = n // 10
print(f'Miracle number is: {m}')