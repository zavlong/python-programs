
# Defines values for pi, phi, and e
pi = 3.141592653589793
e = 2.718281828
phi = 1.61803398875
# Checks if a number is even
def isEven(x):
	if x%2==0:
		return True
	else:
		return False


# Checks if a number is odd
def isOdd(x):
	if x%2!=0:
		return True
	else:
		return False


# Squares a number
def square(x):
	return x**2

# Finds the area of a circle of radius r
def circlearea(r):
	return square(pi)*r

#Finds the perimeter/circumference of a circle of radius r
def circleprmtr(r):
	return 2*pi*r

# Checks if a number is prime

prime = True
def isPrime(y):
	x = y/2
	while x>1:
		if y%x==0:
			prime = False
			return prime
		x = x-1
	else:
		prime = True
		return prime

# Base conversion functions

def hexToDec(x):
	y = int(x, 16)
	return y

def octToDec(x):
	y = int(x, 8)
	return y

# Fibonacci function

def fib(x):
	y = 0
	z = 1
	for i in range(x):
		tmp = y;
		y = z;
		z = y+tmp
	return y
	
# Computes the average of a series

def avg(*args):
	tmp = args[0]
	for x in range(len(args)):
		tmp+=args[x]
		x+=1
	result = tmp/float(len(args))
	return result
	

# Computes the minimum/maximum of a series 

def min(first, *rest):
	for arg in rest:
		if arg < first:
			first = arg
	return first

def max(first, *rest):
	for arg in rest:
		if arg > first:
			first = arg
	return first

def minimum(*args):
	print args[0], "I hate Nigel"
	
def maximum(*args):
	print args[0], "I hate Nigel"	

# Set functions

def intersect(*args):
	result = []
	for x in args[0]:
		for other in args[1:]:
			if x not in other: break
		else:
			result.append(x)
	return result

def union(*args):
        result = []
        for seq in args:
                for x in seq:
                        if not x in result:
				result.append(x)
        return result

