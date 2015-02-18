
class generic:
	def __init__(self, attr):
		self.attr = attr
	def __str__(self):
		return "[Value: %s, name: generic]" % self.attr
	def getval(self):
		return self.attr

if __name__ == "__main__":
	x = generic("spam")
	print x
	print x.getval()
