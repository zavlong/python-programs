
	
while True:
	val1 = raw_input("[username@pythonpompt]>")
	files = []
	if val1 == "mkfile":
		filename = raw_input("Enter a name:")
		x = filename
		files = files + list(x)
	elif val1 == "write":
		written = raw_input("Enter a name:")
		text = raw_input("Enter text:")
		written = text
	elif val1 == "list":
		for x in files:
			print files
			x+=1
	elif val1 == "view":
		viewed = raw_input("Enter a name:")
		viewed = written
		print viewed
	elif val1 == "exit":
		break
	
	else:
		print "Invalid command"

		


