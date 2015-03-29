def getMaxPrime(n, start=2):
	for i in range(start, n+1):
		if n%i==0:
				if i<=n//i:
					return getMaxPrime(n//i, i+1)
				else:
					if n!=i:
						return n//i
	return n
