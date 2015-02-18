
# Defines a Rectangle class

class Rectangle:

	# Shared constructor definition

	def __init__(self, x, y, w, h):
		self.x = x;
		self.y = y;
		self.w = w;
                self.h = h;

	# Overloaded operator methods

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

	# Display method definition (with unicode)

	def display(self):
		print u"\u250C"+(u"\u2500"*((int(self.w)*2)-1))+u"\u2510"
		print (u"\u2502"+" "*((int(self.w-1)*2)+1)+u"\u2502\n")*int(self.h),
		print u"\u2514"+(u"\u2500"*((int(self.w)*2)-1))+u"\u2518"

# Defines a CurvedRectangle class inheriting from Rectangle

class CurveRectangle(Rectangle):

	# Custom methods (overrides those in superclass)

        def __str__(self):
                return "[CurveRectangle instance: x= %f, y=%f, w=%f, h=%f]" % (self.x, self.y, self.w, self.h)
        def __add__(self, other):
                return CurveRectangle(float(self.x)+other.x,float(self.y)+other.y,float(self.w)+other.w,float(self.h)+other.h)
        def __sub__(self, other):
                return CurveRectangle(float(self.x)-other.x,float(self.y)-other.y,float(self.w)-other.w,float(self.h)-other.h)
        def __mul__(self, other):
                return CurveRectangle(float(self.x)*other.x,float(self.y)*other.y,float(self.w)*other.w,float(self.h)*other.h)
        def __div__(self, other):
                return CurveRectangle(float(self.x)/other.x,float(self.y)/other.y,float(self.w)/other.w,float(self.h)/other.h)


        def display(self):
                print u"\u256D"+(u"\u2500"*((int(self.w)*2)-1))+u"\u256E"
                print (u"\u2502"+" "*((int(self.w-1)*2)+1)+u"\u2502\n")*int(self.h),
                print u"\u2570"+(u"\u2500"*((int(self.w)*2)-1))+u"\u256F"

# Defines a CurvedRectangle class inheriting from Rectangle

class FillRectangle(Rectangle):

	# Custom methods (overrides those in superclass)

	def __str__(self):
                return "[FillRectangle instance: x= %f, y=%f, w=%f, h=%f]" % (self.x, self.y, self.w, self.h)
        def __add__(self, other):
                return FillRectangle(float(self.x)+other.x,float(self.y)+other.y,float(self.w)+other.w,float(self.h)+other.h)
        def __sub__(self, other):
                return FillRectangle(float(self.x)-other.x,float(self.y)-other.y,float(self.w)-other.w,float(self.h)-other.h)
        def __mul__(self, other):
                return FillRectangle(float(self.x)*other.x,float(self.y)*other.y,float(self.w)*other.w,float(self.h)*other.h)
        def __div__(self, other):
                return FillRectangle(float(self.x)/other.x,float(self.y)/other.y,float(self.w)/other.w,float(self.h)/other.h)

	def display(self):
		print u"\u2593"+(u"\u2593"*((int(self.w)*2)-1))+u"\u2593"
                print (u"\u2593"+u"\u2593"*((int(self.w-1)*2)+1)+u"\u2593\n")*int(self.h),
                print u"\u2593"+(u"\u2593"*((int(self.w)*2)-1))+u"\u2593"


# Run if not imported

if __name__ == "__main__":
	print "=====             "
	print "  |      ||    || "
	print "  |     ====  ===="
	print "=====    ||    || "

