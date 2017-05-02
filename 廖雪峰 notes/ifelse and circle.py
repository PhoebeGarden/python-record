age = 20
if age >= 18:
	print('your age is', age)
	print('adult')
elif age >= 6:
	print('teenager')
else:
    print('kid')	

s = 333
#s = input('birth: ')
birth = int(s)
if birth < 2000:
	print('00前')
else:
	print('00后')

#练习
heigth = 1.75
weigth = 80.5
bmi = weigth/(heigth*heigth)
print('bmi =', bmi)
if bmi < 18.5:
	print('过轻')
elif bmi < 25:
	print('正常')
elif bmi < 28:
	print('过重')
elif bmi < 32:
	print('肥胖')
else:
    print('严重肥胖')

#循环
sum = 0
for x in range(1,101):
	print(x)
	sum = sum + x
print('sum =', sum)

sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print(sum)

#练习
L = ['Bart', 'Lisa', 'Adam']
for name in L:
	print('Hello,', name)

#break
n = 0
while n <= 100:
	if n > 10:
		break
	print(n)
	n = n + 1
print('END')

#continue
n = 0
while n < 10:
	n = n + 1
	if n % 2 == 0:
		continue
	print(n)
