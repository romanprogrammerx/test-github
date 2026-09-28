#A1:
width = 17 # ширина
height = 12.0 # высота
#1.
print(width//2)
#2. 
print(width/2.0)
#3.
print(height/3)
#4. 
print(1 + 2 * 5)
#A2: 
#7.
print(int('42'))
#A3:
degree = 1921000
mbite = degree/(1024*1024)
print(mbite)

a=int(input("число а: "))
b=int(input("число b: "))
if a>b:
	print(a)
else:
	print(b)
if a==b:
	print("числа равны ")
else:
	print("числа не равны ")

if a%b>0:
	print("NO")
else:
	print("YES")

t=int(input())
h=t//3600
m=(t%3600)//60
s=t%60
print("{:02}:{:02}:{:02}".format(h, m, s))

a=int(input())
b=int(input())
c=int(input())
d=int(input())
if (a+c)%2==(b+d)%2:
	print("YES")
	if (a+c)%2==0:
		print("Black")
	else:
		print("White")
else:
	print("NO")
	



