import itertools

class Factor(object):

	def __init__(self,vars=[None]):
		
		self.vars = vars

	def set_factor_names(self):
		# 1. get factor names
		print('Enter alphanumeric factor names separated by spaces')
		factor_names = input().split()
		self.vars = tuple(factor_names)
		print('Factor names are: {}'.format(factor_names))

	def set_cardinalities(self):
		# 2. get cardinalities
		while True:
			print('Enter cardinality of these {} factors as integers'.format(len(self.vars)))
			
			try:
				factor_cardinalities = input().split()
				card_int = [int(x) for x in factor_cardinalities]
			except ValueError:
				print('Invalid input, please enter integers bigger than zero')
				continue

			if len(card_int)!=len(self.vars):
				print('Enter the same exact number of cardinalities as there are factors, {}'.format(len(self.vars)))
				continue
			else:
				self.card = card_int
				# and automatically populate the assignments:
				self.create_assignments()
				self.nvals = len(self.assignments)
				break

	def create_assignments(self):
		# 3. create assignments, note the first variable iterates the fastest
		reversed_cardinalities = self.card[::-1]
		assignment_generator = itertools.product(*map(range,reversed_cardinalities))
		self.assignments = [x[::-1] for x in assignment_generator]

	def set_values(self):
		# 4. set values of assignments 
		self.values = []
		for assignment in self.assignments:
			while True:
				try:
					inp = input('Enter value of assignment {}'.format(assignment))
					self.values.append(float(inp))
					break
				except ValueError:
					print('Please enter a number')