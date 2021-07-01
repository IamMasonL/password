p = "a123456"
t = 3

while t > 0:
	a = input("請輸入密碼: ")
	if a == p:
		print("登入成功")
		break
	else:
		t = t - 1
		if t == 0:
			print("登入失敗!")
		else:
			print("密碼錯誤! 還剩", t, "次機會")