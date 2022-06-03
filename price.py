num = int(input("Nhập giá: "))
if num >= 150:
	print("Tổng: ", num - 50)
elif num >= 100:
	print("Tổng: ", num - 25)
elif num >= 75:
	print("Tổng: ", num - 15)
else:
    print("Tổng: ", num)