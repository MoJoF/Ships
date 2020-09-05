from random import randint

class Fight:
	def __init__(self, name1, name2, damage1, damage2, health1, health2):
		self.name1 = name1
		self.name2 = name2
		self.damage1 = damage1 * randint(0, 10)
		self.damage2 = damage2 * randint(0, 10)
		self.health1 = health1
		self.health2 = health2

	def fight(self):
		while(self.health1 < 0 or self.health2 < 0):
			# Attack
			self.health1 -= self.damage2
			print(f"{self.name2} нанёс {self.damage2} урона. У {self.name1} осталось {self.health1} прочности")

			# Defense
			self.health2 -= self.damage1
			print(f"{self.name1} нанёс {self.damage1} урона. У {self.name2} осталось {self.health2} прочности")

		if (self.health1 < 0):
			print(f"{self.name1} потоплен игроком {self.name2}.")

		elif (self.health2 < 0):
			print(f"{self.name2} потоплен игроком {self.name1}.")