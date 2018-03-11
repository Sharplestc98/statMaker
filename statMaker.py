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
	
	def __init__(self):
		print "\n\n   <<  Hello! Welcome to statMaker v0.1!  >>"
		print "   <<Please enter a command to get started>>\n"
		self.shell()
		
	def getAttributes(self):
		print self.pad(self.space)+"|",
		for x in range(0, 6):
			print self.attribute(),"|",
		print ""
			
	def getHitPoint(self,numSides,modifier):
		try:
			if int(modifier) > 0:
				mod = "+"+modifier
			elif int(modifier) < 0:
				mod = modifier
			else:
				mod = ""
			print self.pad(self.space)+"Hit Point Increment = 1d"+numSides+mod," = ",self.hitPoints(int(numSides),int(modifier))
		except ValueError:
			print self.pad(self.space)+"<<wrong data type given, please type 'help' to see correct data types>>"
		
	def attribute(self):
		l = []
		for x in range(0, 4):
			l.append(self.rollDice(6))
		l.remove(min(l))
		return sum(l)
	
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
	
	def rollDice(self, numSides):
		roll = random.randint(1,numSides)
		return roll
		
	def hitPoints(self,numSides,modifier):
		return self.rollDice(numSides)+modifier
	
	def pad(self,num):
		return " "*num
		
	def help(self):
		print self.pad(self.space)+"'exit'                   - leaves the program"
		print self.pad(self.space)+"'atr'                    - creates 6 atrribute variables"
		print self.pad(self.space)+"'hp <number> <number>'   - returns a value to increment your hp by"
		print self.pad(self.space)+"'roll' <number>          - returns a dice roll of the number of sides given"
	
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
					if len(input)==2:
						self.getHitPoint(input[1],"0")
					elif len(input)==3:
						self.getHitPoint(input[1],input[2])
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