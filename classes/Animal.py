class Animal:
	def __init__(self, name):
		self.name = name

	def get_name(self):
		return self.name

class Cat(Animal):
	def __init__(self, name):
		super().__init__(name)
		self._purr_sound = 'purr purr purr'

	def purr(self):
		print(self._purr_sound)
