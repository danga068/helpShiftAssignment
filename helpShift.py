import re


class helpShift():
	def __init__(self):
		print "ashok"
		pass

	def searchContact(self, newName):
		result = []
		with open('contacts') as f:
			for line in f:
				name = line.strip()
				divideName = name.split(' ')
				firstName = divideName[0]

				if len(divideName) > 1:
					lastName = divideName[1]
				else:
					lastName = ''

				if name == newName:
					result.append({'name': name, 'priority': 1})
				elif re.match(newName, firstName):
					result.append({'name': name, 'priority': 2})
				elif re.match(newName, lastName):
					result.append({'name': name, 'priority': 3})

		finalResult = sorted(result, key=lambda k: k['priority'])
		return finalResult


	def addContact(self, name):
		target = open('contacts', 'a')
		target.write(name + '\n')
		target.close()


	def printResult(self, result):
		if result:
			for name in result:
				print name['name']
		else:
			print "result not found"


if __name__ == "__main__":
	h = helpShift()

	while(True):
		print '1) Add contact 2) Search 3) Exit'

		try:
			op = int(raw_input())
			if op == 1:
				newName = raw_input("Enter name: ")
				h.addContact(newName)

			elif op == 2:
				newName = raw_input("Enter name: ")
				matchedNames = h.searchContact(newName)
				h.printResult(matchedNames)

			elif op == 3:
				print 'Happy Searching'
				break

		except ValueError:
			print "That's not an int!"
