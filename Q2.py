def Fibonacci(n):
	if(n==2): 
		return 2;
	elif(n==1):
		return 1;	
	return Fibonacci(n-1)+Fibonacci(n-2)
	
def Find():
	i=1;
	sum=0;
	while(Fibonacci(i)<=4000000):
		if(Fibonacci(i)%2==0):
			sum+=Fibonacci(i)
		i+=1
	print(sum)
