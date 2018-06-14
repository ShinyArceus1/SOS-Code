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

def shinydebug statesetup()
	global debugenabled
	debugenabled = false
shinydebug_statesetup()
def debugstate(state)
	if state == 'enable':
		debugenabled = True
		print('debug mode has been enabled')
	elif state =='disable':
		debugenabled = False
		print('debug mode has been disabled')
	else:
		raise RuntimeError('An Error Has Occured: Invalid Debug State Entered (0005)')
def shinydebug_Varglobal():
	if debugenabled is True:
		global sos_output
		global sos_Stored
	else:
		raise RuntimeError('An Error Has Occured:Debug mode is not enabled(0006)')
def shinydebug_Supresswarning():
	if debugenabled is True:
		import warnings
		warnings.filterwarnings("ignore")
	else:
		raise RuntimeError('An Errror Has Occured:Debug mode Not Enabled(0006)')

def shinyexecution(exitcode=0)
	import sys
	sys.exit(exitcode)
