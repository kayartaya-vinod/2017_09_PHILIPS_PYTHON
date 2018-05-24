class Vehicle(object):
	def __init__(self):
		print("Vehicle __init__ called")

	def info(self):
		print("INFO:: Vehicle class by Vinod")

class Flyable(object):
	def __init__(self):
		print("Flyable __init__ called")

	def info(self):
		print("INFO:: Flyable class by Vinod")

class Car(Vehicle):
	def __init__(self):
		super().__init__()
		print("Car __init__ called")

	def info(self):
		print("INFO:: Car class by Vinod")

class Helicopter(Vehicle,Flyable):
	def __init__(self):
		# super().__init__()
		# whem multiple inheritance is involved,
		# use the explit constructor calls
		Vehicle.__init__(self)
		Flyable.__init__(self)
		print("Helicopter __init__ called")


def main():
	c1 = Car()
	c1.info()

	print()

	h1 = Helicopter()
	h1.info()
	print()
	
	Vehicle.info(h1)
	Flyable.info(h1)

if __name__ == '__main__':
	main()













