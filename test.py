import unittest
from helpShift import helpShift


h = helpShift()

class MyTest(unittest.TestCase):

	def test_searchContact(self):
		self.assertEqual(len(h.searchContact('Chris')), 4)
		self.assertEqual(len(h.searchContact('Kaitlyn')), 1)
		self.assertEqual(len(h.searchContact('Rowell')), 2)
		
		reultList = h.searchContact('Chris')
		names = []
		for result in reultList:
			names.append(result['name'])
		
		self.assertEqual(names, ['Chris', 'Chris Harris', 'Chris Cairns', 'Chris Rowell'])



unittest.main()