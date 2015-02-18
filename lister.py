


def listing(module, verbose):
	if verbose != 0:
		print "-"*30
		print "name:", module.__name__, "file:", module.__file__
		print "-"*30
		count = 0
		for attr in module.__dict__.keys():
			print "%d: %s" % (count, attr),
			if attr[0:2]!="__":
				print getattr(module, attr)
			print "\n"
			count+=1
		print "-"*30
		print module.__name__, "has %d names" % count
		print "-"*30
	else:
		print "name:", module.__name__, "file:", module.__file__

