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

#tan of a number
def shinytan(number):
	import math
	return math.tan(number)

#hypot of a number
def shinyhypot(number):
	import math
	return math.hypot(number)

#atan of a number
def shinyatan(number):
	import math
	return math.atan(number)

#asin of a number
def shinyasin(number):
	import math
	return math.asin(number)

#get value of pi
def shinepi():
	import math
	return math.pi

#get value of e
def shinye():
	import math
	return math.e

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

#setup debugenabled variable
def shinydebug_statesetup():
	global debugenabled
	debugenabled = False

#execute shinydebug_statesetup()
shinydebug_statesetup()

#change debug state
def debugstate(state):
	if state == 'enable':
		debugenabled = True
		print('debug mode has been enabled')
	elif state =='disable':
		debugenabled = False
		print('debug mode has been disabled')
	else:
		raise RuntimeError('An Error Has Occured: Invalid Debug State Entered (0005)')

#make variables global
def shinydebug_varglobal():
	if debugenabled is True:
		global sos_output
		global sos_stored
	else:
		raise RuntimeError('An Error Has Occured:Debug mode is not enabled(0006)')

#supresswarnings
def shinydebug_supresswarning():
	if debugenabled is True:
		import warnings
		warnings.filterwarnings("ignore")
	else:
		raise RuntimeError('An Errror Has Occured:Debug mode Not Enabled(0006)')

#exit execution
def shinyexecution(exitcode=0):
	import sys
	sys.exit(exitcode)

#set the given value to sos_output and return it
def shineput(value):
	sos_output = value
	return value

#store a value
def shinestore(value):
	sos_stored = value

#get the stored value
def shineget(value):
	return sos_stored
