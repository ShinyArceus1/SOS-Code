#paragraph space
def shinyspace(paragraphspaces=1):
	for i in range(paragraphspaces):
		print("", end="/n")

#print letters/numbers
def shineprint(message):
	print(str(message))

#execute
def shinecute(command):
	exec(command)

#evaluate
def shinevaluate(operation):
	return eval(operation)

#absolute
def shinelute(operation):
	return abs(operation)

#sin of a number
def shinysin(number):
	import math
	return math.sin(number)

#divide 2 numbers
def shinedivide(firstnumber, secondnumber):
	return firstnumber / secondnumber

#multiply 2 numbers
def shinetimes(firstnumber, secondnumber):
	return firstnumber * secondnumber

#add 2 numbers
def shineadd(firstnumber, secondnumber):
	return firstnumber + secondnumber

#minus 2 numbers
def shineminus(firstnumber, secondnumber):
	return firstnumber - secondnumber
