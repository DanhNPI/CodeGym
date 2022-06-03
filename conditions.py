num = int(input('Nhập số nguyên: '))

result = "Even" if num%2 == 0 else "Odd"

print (result)

'-------------------------------------------'

num = float(input('Nhập số: '))

if num%2 == 0:
    print('Even')
elif num%2 == 1:
    print ('Odd')
else:
    print ('Not Even Not Odd!')