class only_int_arguments(object):
	def __init__(self, original_function):
		self.of = original_function
		
	def __call__(self, *args):
		try:
			[arg/1 for arg in list(args)]
		except TypeError:
			raise ValueError
		return self.of(*args)

@only_int_arguments
def sum_integers(*args):
	return sum(list(args))


def create_database(db_name):
	#create_directory(db_name)
	pass

def use(db_name):
	return TinyDatabase(db_name)


# Usage:

pyp_database.create_database('imdb')
db = Database('imdb')


print sum_integers(4,5,"c")