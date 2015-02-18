# Swaps two values

def swap(x, y):
	x, y = y, x
	return x, y

# Reverses a sequence

def reverse(l):
	res = l[:]
	for x in range(len(res)):
		tmp = res[x]
		res[x] = res[(x*-1)-1]
		res[(x*-1)-1] = tmp
		x+=1
	return res

