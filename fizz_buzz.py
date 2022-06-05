num1 = int(input('Nhập số thứ nhất: '))

num2 = int(input('Nhập số thứ hai: '))

if num1 > num2:
    print ('Error!!!')
else:
    for i in range(num1, num2+1):
        if i%3 == 0:
            print (i)
            print ('Fizz')
        if i%5 == 0:
            print (i)
            print ('Buzz')
        if i%3 == 0 and i%5 == 0:
            print (i)
            print ('FizzBuzz')


        