num = int(input('Введите число: '))
result = ''
for i in range(1, num):
    for j in range(i+1, num):
        if num % (i+j) == 0:
            result += f'{i}{j}'
print(f'{num} - {result}')