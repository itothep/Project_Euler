
def Palindrome(start):
	for i in range(start, 1000000):
		if i/11=0:
			if i//100000==0:
				n1=i//10000
				n2=(i//1000)%10
				n3=(i//100)%10
				n4=(i//10)%10
				n5=i%10
				if n1==n5 and n2==n4:
					return find(i)
			else:
				n1=i//100000
				n2=(i//10000)%10
				n3=(i//1000)%10
				n4=(i//100)%10
				n5=(i//10)%10
				n6=i%10
				if n1==n6 and n2==n5 and n3==n4:
						return find(i)
	return 0

def find(n):
	for a in range(100, 1000):
		for b in range(100, 1000):
			if a*b==n and a!=b:
				print(a)
				print(b)
				print(n)
				print("--")
				return Palindrome(n+1)
	return Palindrome(n+1)
