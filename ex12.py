from ex11 import Person

class Employee(Person):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		# Person.__init__(self, **kwargs)
		
		self.__salary = kwargs["salary"] if "salary" in kwargs else None
		self.__dept = kwargs["dept"] if "dept" in kwargs else "ADMIN"
	
	@property
	def salary(self):
		return self.__salary
	@salary.setter
	def salary(self, salary):
		if(salary<0):
			raise ValueError("Negative salary!")
		self.__salary = salary

	@property
	def dept(self):
		return self.__dept
	@dept.setter
	def dept(self, dept):
		self.__dept = dept

	# overriding
	def info(self):
		Person.info(self)
		print("salary =", self.__salary)
		print("dept =", self.__dept)
		print()
		# super().info()

	def __lt__(self, value):
		return self.__salary < value

	def __le__(self, value):
		return self.__salary <= value

	def __gt__(self, value):
		return self.__salary > value

	def __ge__(self, value):
		return self.__salary >= value

	def __iadd__(self, value):
		if type(value) in (int, float):
			self.salary += value
		elif type(value) == str:
			self.name += value
		else: raise TypeError("Invalid type: Only int, float, str allowed")

		# return self in __ixxx__ functions
		return self

def main():
	e1 = Employee(name="Scott", city="Dallas", salary=34000)
	e1.info()

	print("e1 < 30000 is", (e1 < 30000))
	print("e1 < 40000 is", (e1 < 40000))
	e1 += 5000 # 5000 should be added to salary
	e1 += " John" # " John" appended to name
	e1.info()

	# e1 < 40000 should indicate --> e1.is_salary_lessthan(40000)

if __name__ == '__main__':
	main()









