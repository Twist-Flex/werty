class Mammals:
	def __init__(self, name, habitat, food, propereties):
		self.name = name
		self.habitat = habitat
		self.food = food
		self.propereties = propereties

	def eat(self,food):
		res = "{0.name} поел(а) {1}".format(self, food )
		print(res)

	def say(self):
		print("Однако здравствуйте")


class Cat(Mammals):
	def say(self):
		print("Мяу миаоу ня нгеонг")


class Dog(Mammals):

	def __init__(self, name, habitat, food, propereties, bark_loughtne):

		self.name = name
		self.habitat = habitat
		self.food = food
		self.propereties = propereties
		self.bark_loughtne = bark_loughtne

	def eat(self,food):
		res = "{0.name} поел(а) {1}".format(self, food )
		print(res)

	def bark(self):
		if self.bark_loughtne < 1000:
			print("Гав-Гав")
		else:
			print("Грааааааааааааааар")

	def eat(self, food):
		print("И разорвала"+ self.food + " на куски ")

selection = input("""Выберите вид:
1)Домосед  
2)Мусорщик\n  """)

name = input("""Выберите имя: """)

cat = Cat(name=name, habitat=selection, food="рыба", propereties="дом")
print(cat.name)
cat.eat("Мясо")
cat.say()

dog = Dog(name="Саид",habitat="Каспийск",food="Картошка",propereties="Общяга",bark_loughtne="Алкаш")
dog.bark()