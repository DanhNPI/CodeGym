import math

weight = float(input('Nhập cân nặng (kg): '))
height = float(input('Nhập chiều cao (m): '))

BMI = weight/(math.pow(height, 2))

'''BMI < 16: Gầy cấp độ III
16 <= BMI < 17:  Gầy cấp độ II
17<= BMI < 18.5: Gầy cấp độ I
18.5 <= BMI < 25: Bình thường
25 <= BMI < 30: Thừa cân
30 <= BMI < 35 : Béo phì cấp độ I
35 <= BMI < 40: Béo phì cấp độ II
BMI > 40: Béo phì cấp độ III'''

if BMI < 16:
    result = 'Gầy cấp độ III'
elif BMI <17: 
    result = 'Gầy cấp độ II'
elif BMI < 18:
    result = 'Gầy cấp độ I'
elif BMI < 25:
    result = 'Bình thường'
elif BMI < 30:
    result = 'Thừa cân'
elif BMI < 35:
    result = 'Béo phì cấp độ I'
elif BMI < 40:
    result = 'Béo phì cấp độ II'
else:
    result = 'Béo phì cấp độ III'

print ('Chỉ số BMI: ', BMI)
print ('Kết quả: ', result)