def shinyspace(paragraphspaces=1):
	for i in range(paragraphspaces):
		print("", end="/n")

def shineprint(message):
	print(str(message))

def shinecute(command):
	exec(command)

def shinevaluate(operation):
	return eval(operation)

def shinelute(operation):
	return abs(operation)
