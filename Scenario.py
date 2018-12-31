class Scenario:
	def __init__(self, name, info, tests):
		self.Name = name
		self.Info = info
		self.Tests = tests
	def AddTest(self, test):
		self.Tests.append(test)