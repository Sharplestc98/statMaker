import random
import sys

'''
A simple python program that enables the user to make some simple
dnd dice rolling functions simpler. Such as rolling for attributes
or your next amount of hit points

Author: Thomas Christopher Sharples
'''
class statMaker:
	
	space = 9
	
	'''
	Class constructor, prints out the starting statments and starts the shell
	'''
	def __init__(self):
		print "\n\n   <<  Hello! Welcome to statMaker v0.1!  >>"
		print "   <<Please enter a command to get started>>\n"
		self.shell()
	
	'''
	Makes a set of attribute scores and prints them out for the user
	'''	
	def getAttributes(self):
		String = "\n"+self.pad(self.space)+"|"
		for x in range(0, 6):
			print self.pad(self.space)+"Attribute: ",x+1
			String = String+str(self.attribute())+"|"
		print String + "\n"
	
	'''
	Makes a hit point increment based on given dice size and modifier. Prints out for the user
	'''	
	def getHitPoint(self,numSides,modifier):
		try:
			if int(modifier) > 0:
				mod = "+"+modifier
			elif int(modifier) < 0:
				mod = modifier
			else:
				mod = ""
			print self.pad(self.space)+"Hit Point Increment = 1d"+numSides+mod," = ",self.rollDice(int(numSides))+int(modifier)
		except ValueError:
			print self.pad(self.space)+"<<wrong data type given, please type 'help' to see correct data types>>"
	
	'''
	Makes a single attribute score by rolling 4 dice and removing the lowest roll
	'''	
	def attribute(self):
		l = []
		for x in range(0, 4):
			num = self.rollDice(6)
			l.append(num)
			print self.pad(self.space*2)+"Dice Roll",x+1," = ",num
		l.remove(min(l))
		return sum(l)
	
	'''
	Makes a dice roll from a given number of dice, dice size and modifier, prints the result
	'''	
	def roll(self,numSides,numDice,modifier):
		try:
			total = 0 + int(modifier)
			for x in range(0, int(numDice)):
				num = self.rollDice(int(numSides))
				print self.pad(self.space)+"Dice Roll",x+1," = ",num
				total = total + num
			total = total
			print self.pad(self.space)+"Rolling "+numDice+"d"+numSides+"+"+modifier+" Result = ",total 
		except ValueError:
			print self.pad(self.space)+"<<wrong data type given, please type 'help' to see correct data types>>"
	
	'''
	Rolls a single dice of a given size, returns the result
	'''	
	def rollDice(self, numSides):
		roll = random.randint(1,numSides)
		return roll
	
	'''
	Pads the string with a given number of spaces
	'''	
	def pad(self,num):
		return " "*num
		
	'''
	Prints out the help message to the shell
	'''		
	def help(self):
		print self.pad(self.space)+"'exit'                   - leaves the program"
		print self.pad(self.space)+"'atr'                    - creates 6 atrribute variables"
		print self.pad(self.space)+"'hp <number> <number>'   - returns a value to increment your hp by"
		print self.pad(self.space)+"'roll' <number>          - returns a dice roll of the number of sides given"
	
	'''
	Breaks up a dice string into its component parts so it can be used by the
	roll dice function
	'''
	def breakUpString(self,String):
		temp=String
		dPos = temp.find("d")
		plusPos = temp.find("+")
		minusPos = temp.find("-")
		if temp[0]!="d":
			numDice = temp[0:dPos]
		else:
			numDice = "1"
		if minusPos > -1:
			modifier = "-"+temp[minusPos+1:len(temp)]
			numSides = temp[dPos+1:minusPos]
		elif plusPos > -1:
			modifier = temp[plusPos+1:len(temp)]
			numSides = temp[dPos+1:plusPos]
		else:
			modifier = "0"
			numSides = temp[dPos+1:len(temp)]
		return numSides,numDice,modifier
	
	'''
	Starts and handles the shell
	'''	
	def shell(self):
		while True:
			try:
				input = raw_input("   > ").split()
				if not input:
					print self.pad(self.space)+"<<No input given, please enter a command or type 'help'>>"
					self.shell()
				if input[0] == "exit":
					sys.exit(1)
				elif input[0] == "atr":
					self.getAttributes()
				elif input[0] == "hp":
					numSides,numDice,modifier = self.breakUpString(input[1])
					self.getHitPoint(numSides,modifier)
				elif input[0] == "help":
					self.help()
				elif input[0] == "roll":
					numSides,numDice,modifier = self.breakUpString(input[1])	
					self.roll(numSides,numDice,modifier)
				else:
					print self.pad(self.space)+"<<Input not recognised, type 'help' to see all commands>>"
			except IndexError:
				print self.pad(self.space)+"<<Not enough parameters given for function>>"
				
s = statMaker()		