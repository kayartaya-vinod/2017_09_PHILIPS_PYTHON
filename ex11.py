# Working with user defined classes

def main():
	p1 = Person(name="Vinod", email="vinod@vinod.co")
	p1.info()

	p2 = Person(name="John Doe", city="Dallas")
	p2.__email = "johndoe@mail.com" # new public member
	p2.info()
	print("p2.__email is", p2.__email)


	p3 = Person(name="Vinod", email="vinod@vinod.co")
	print("Name = {}, city = {}, email = {}".format(
		p3.name, p3.city, p3.email))

	p3.name = "Vinod KK" # invoking the setter property method
	p3.email = "vinod@kvinod.com"
	p3.city = "Bengaluru"

	p3.info()

	


class Person(object):
	def __init__(self, **kwargs):
		# members starting with __ (and not ending with) are
		# treated as private
		self.__name = kwargs["name"] if "name" in kwargs else None
		self.__email = kwargs["email"] if "email" in kwargs else None
		self.__city = kwargs["city"] if "city" in kwargs else "Bangalore"

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		if type(name)!=str:
			raise TypeError("Invalid type for name. Use <str>")
		self.__name = name

	@property
	def city(self):
		return self.__city

	@city.setter
	def city(self, city):
		self.__city = city

	@property
	def email(self):
		return self.__email

	@email.setter
	def email(self, email):
		self.__email = email

	def info(self):
		print("name =", self.__name)
		print("city =", self.__city)
		print("email =", self.__email)









if __name__ == '__main__':
	main()
