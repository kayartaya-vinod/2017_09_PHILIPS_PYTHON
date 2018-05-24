# Working with function args

def print_info(name, city, email, phone, **kwargs):
	print("name =", name)
	print("city =", city)
	print("email =", email)
	print("phone =", phone)

	for k in kwargs.keys():
		print("{} = {}".format(k, kwargs[k]))
	
	print("-"*25)


print_info("Vinod", "Bangalore", "vinod@vinod.co", "9731424784")

t1 = ["John Doe", "Dallas", "johndoe@mail.com", "5557373222"] # can be a tupe or even a set, but set is not ordered, hence no guarantee of the parameter sequence

print_info(*t1) # unbox the list and send them as individual parameters

d1 = dict(name="Jane Doe", 
	email="janedoe@mail.com", 
	phone="657222772",
	country="USA",
	gender="Female",
	city="Chicago")

print_info(**d1)

# positional params (named non-default parameters)
# var-args (*args)
# named default parameters
# keyword-args (**kwargs)

def test_fn(name, *args, city="Bangalore", **kwargs):
	print("name = ", name)
	print("city = ", city)
	print("args = ", args)
	print("kwargs = ", kwargs)
	print()

# test_fn("Vinod", city="Bangalore")
# test_fn("Vinod", "ISRO Lyt", "Karnataka", city="Bangalore") 
# test_fn("Vinod", "Shivamogga", "ISRO Lyt", "Karnataka")
# test_fn("Vinod", "Bangalore", "ISRO Lyt", "Karnataka", email="vinod@vinod.co", city="Bangalore", country="India")

# test_fn("Vinod", name="kumar", city="Bangalore") # error -> multiple values for a single parameter (positional + named for parameter "name")

# test_fn(name = "Vinod", "Bangalore") # error --> positional parameters can not be used after named parameters








def add_numbers(*args):
	# print("args is", args)
	# print("type of args is", type(args))
	total = 0
	for arg in args:
		if type(arg) in (int, float):
			total += arg

	return total

def create_json(**kwargs):
	# print("kwargs is", kwargs)
	# print("type of kwargs is", type(kwargs))
	import json
	return json.dumps(kwargs)


# total = add_numbers(10, "rama", 20.55, 30, 40, "vinod", "hello")
# print("total =", total, "!")

# json_data = create_json(name="vinod", city="bangalore")
# print(json_data)







