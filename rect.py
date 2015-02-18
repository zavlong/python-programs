
class Rectangle:
	def __init__(self, x, y, w, h):
		self.x = x;
		self.y = y;
		self.w = w;
                self.h = h;
	def __str__(self):
		return "[Rectangle instance: x= %f, y=%f, w=%f, h=%f]" % (self.x, self.y, self.w, self.h)
	def __add__(self, other):
		return Rectangle(float(self.x)+other.x,float(self.y)+other.y,float(self.w)+other.w,float(self.h)+other.h)
	def __sub__(self, other):
                return Rectangle(float(self.x)-other.x,float(self.y)-other.y,float(self.w)-other.w,float(self.h)-other.h)
	def __mul__(self, other):
                return Rectangle(float(self.x)*other.x,float(self.y)*other.y,float(self.w)*other.w,float(self.h)*other.h)
	def __div__(self, other):
                return Rectangle(float(self.x)/other.x,float(self.y)/other.y,float(self.w)/other.w,float(self.h)/other.h)


	def display(self):
		print "-"*((int(self.w+1)*2)-1)
		print ("|"+" "*((int(self.w-1)*2)+1)+"|\n")*int(self.h),
		print "-"*((int(self.w+1)*2)-1)


if __name__ == "__main__":
	print "=====             "
	print "  |      ||    || "
	print "  |     ====  ===="
	print "=====    ||    || "

