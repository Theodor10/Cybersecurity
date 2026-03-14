import string

#naive method
def modInverse(a,m):
	
	for x in range(1,m):
		if (a*x) % m == 1:
			return x

	return -1


# Iterative Python 3 program to find
# modular inverse using extended
# Euclid algorithm

# Returns modulo inverse of a with
# respect to m using extended Euclid
# Algorithm Assumption: a and m are
# coprimes, i.e., gcd(A, M) = 1

#source: GeekforGeeks
def modInverse1(A, M):
	m0 = M
	y = 0
	x = 1

	if (M == 1):
		return 0

	while (A > 1):

		# q is quotient
		q = A // M

		t = M

		# m is remainder now, process
		# same as Euclid's algo
		M = A % M
		A = t
		t = y

		# Update x and y
		y = x - q * y
		x = t

	# Make x positive
	if (x < 0):
		x = x + m0

	return x


with open("message.txt") as file:
	
	content = file.read()
	message  =[int(val) for val in content.split()]
	print (message)

	alphabet = list(string.ascii_uppercase)
	digits = [0,1,2,3,4,5,6,7,8,9]

	decrypted = ['']*len(message)
	i =0
	for x in message:
		
		y = modInverse(x,41) 
		print(y)
		if y <= 26:
			decrypted[i]=alphabet[y-1]

		if y >= 27 and y <= 36:
			decrypted[i]=digits[(y)%27]	
		if y == 37:	
			decrypted[i]='_'

		i+=1


	print("\n")
	print(decrypted)

