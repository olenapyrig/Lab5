class Property:
	'''
	Represents property with data about its square feet, bedrooms and
	baths amount
	'''

	def __init__(self, square_feet='', beds='',
				 baths='', **kwargs):
		super().__init__(**kwargs)
		self.square_feet = square_feet
		self.num_bedrooms = beds
		self.num_baths = baths

	def display(self):
		"""
		(object) -> ()
		This method prints all data about property
		"""
		print("PROPERTY DETAILS")
		print("================")
		print("Square footage: {}".format(self.square_feet))
		print("Bedrooms: {}".format(self.num_bedrooms))
		print("Bathrooms: {}".format(self.num_baths))
		print()

	def prompt_init():
		"""
		() -> (dict)
		Getting property data via input
		"""
		return dict(square_feet=input("Enter the square feet: "),
					beds=input("Enter number of bedrooms: "),
					baths=input("Enter number of baths: "))

	prompt_init = staticmethod(prompt_init)


class Apartment(Property):
	'''Represents detailed apartment info with the help of inheritance'''
	valid_laundries = ("coin", "ensuite", "none")
	valid_balconies = ("yes", "no", "solarium")

	def __init__(self, balcony='', laundry='', **kwargs):
		super().__init__(**kwargs)
		self.balcony = balcony
		self.laundry = laundry

	def display(self):
		"""
		(object) ->                                 # todo
		This method modifies parent init with user input
		"""
		super().display()  # Property method
		print("APARTMENT DETAILS")
		print("laundry: %s" % self.laundry)
		print("has balcony: %s" % self.balcony)

	def prompt_init():
		parent_init = Property.prompt_init()
		laundry = ''
		# Getting data about laundry from user
		while laundry.lower() not in Apartment.valid_laundries:
			laundry = input("What laundry facilities does "
							"the property have? ({})".format(
				", ".join(Apartment.valid_laundries)))
			balcony = ''
		# Getting data about balcony from user
		while balcony.lower() not in Apartment.valid_balconies:
			balcony = input("Does the property have a balcony? "
							"({})".format(
				", ".join(Apartment.valid_balconies)))

		parent_init.update({"laundry": laundry, "balcony": balcony})
		return parent_init

	prompt_init = staticmethod(prompt_init)


def get_valid_input(input_string, valid_options):
	"""
	(str, str) -> str
	This function looks for valid response and returns it
	"""
	input_string += " ({}) ".format(", ".join(valid_options))
	response = input(input_string)
	while response.lower() not in valid_options:
		response = input(input_string)  # todo
	return response


def prompt_init():
	"""
	() ->                                 #todo
	This function updates parent init, adding prompts to it
	"""
	parent_init = Property.prompt_init()
	laundry = get_valid_input(
		"What laundry facilities does "
		"the property have? ",
		Apartment.valid_laundries)
	balcony = get_valid_input(
		"Does the property have a balcony? ",
		Apartment.valid_balconies)
	parent_init.update({
		"laundry": laundry,
		"balcony": balcony
	})
	return parent_init


prompt_init = staticmethod(prompt_init)


class House(Property):
	"""
	Represents house by it`s type and available annexes and is son-class  #todo
	"""
	valid_garage = ("attached", "detached", "none")
	valid_fenced = ("yes", "no")

	def __init__(self, num_stories='', garage='', fenced='', **kwargs):
		super().__init__(**kwargs)
		self.garage = garage
		self.fenced = fenced
		self.num_stories = num_stories

	def display(self):
		"""
		(object) -> ()
		This method prints all data about house
		"""
		super().display()
		print("HOUSE DETAILS")
		print("# of stories: {}".format(self.num_stories))
		print("garage: {}".format(self.garage))
		print("fenced yard: {}".format(self.fenced))

	def prompt_init():
		"""
		() -> parent_init
		This method updates parent init, adding prompts to it
		"""
		parent_init = Property.prompt_init()
		fenced = get_valid_input("Is the yard fenced? ", House.valid_fenced)
		garage = get_valid_input("Is there a garage? ", House.valid_garage)

		num_stories = input("How many stories? ")
		parent_init.update({
			"fenced": fenced,
			"garage": garage,
			"num_stories": num_stories
		})
		return parent_init

	prompt_init = staticmethod(prompt_init)


class Purchase:
	'''Represents purchase info'''

	def __init__(self, price='', taxes='', **kwargs):
		super().__init__(**kwargs)
		self.price = price
		self.taxes = taxes

	def display(self):
		"""
		(object) -> ()
		This method prints all data about purchase
		"""
		super().display()
		print("PURCHASE DETAILS")

		print("selling price: {}".format(self.price))
		print("estimated taxes: {}".format(self.taxes))

	def prompt_init():
		"""
		() -> dict
		This method returns dictionary with purchase price and taxes
		"""
		return dict(price=input("What is the selling price? "),
					taxes=input("What are the estimated taxes? "))

	prompt_init = staticmethod(prompt_init)


class Rental:
	'''Represents rental details'''

	def __init__(self, furnished='', utilities='',
				 rent='', **kwargs):
		super().__init__(**kwargs)
		self.furnished = furnished
		self.rent = rent
		self.utilities = utilities

	def display(self):
		"""
		(object) -> ()
		This method prints out data about rental"""
		super().display()
		print("RENTAL DETAILS")
		print("rent: {}".format(self.rent))
		print("estimated utilities: {}".format(
			self.utilities))
		print("furnished: {}".format(self.furnished))

	def prompt_init():
		"""
		() -> (dict)
		This method returns dictionary with rental options as keys
		"""
		return dict(
			rent=input("What is the monthly rent? "),
			utilities=input("What are the estimated utilities? "),
			furnished=get_valid_input("Is the property furnished? ",
									  ("yes", "no")))

	prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
	'''This class represents all details about house and it`s rental'''

	def prompt_init():
		"""
										# todo
		This method calls House class prompts and updates init with
		Rental class prompts
		"""
		init = House.prompt_init()
		init.update(Rental.prompt_init())
		return init

	prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
	def prompt_init():
		"""
		This method calls Apartment class prompts and updates it with
		Rental class prompts
		"""
		init = Apartment.prompt_init()
		init.update(Rental.prompt_init())
		return init

	prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
	def prompt_init():
		"""
		This method calls Apartment class prompts and updates it with
		Purchase class prompts
		"""
		init = Apartment.prompt_init()
		init.update(Purchase.prompt_init())
		return init

	prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
	def prompt_init():
		"""
		This method calls House class prompts and updates it with
		Purchase class prompts
		"""
		init = House.prompt_init()
		init.update(Purchase.prompt_init())
		return init

	prompt_init = staticmethod(prompt_init)


class Agent:
	'''
	This class represents info about properties with their prices and etc.
	'''

	def __init__(self):
		self.property_list = []

	def display_properties(self):
		"""
		This method displays property`s details
		"""
		for property in self.property_list:
			property.display()

	type_map = {
		("house", "rental"): HouseRental,
		("house", "purchase"): HousePurchase,
		("apartment", "rental"): ApartmentRental,
		("apartment", "purchase"): ApartmentPurchase
	}

	def prompt_start():
		"""
		Ask the user whether they want to start the program
		"""

		s = input("Do you want to start using the program?(yes,no) " )
		if s == 'yes':
			return True
		else:
			return False

	prompt_start = staticmethod(prompt_start())

	def add_property(self):
		"""
		This function adds property with all details and makes it an object of
		a certain class
		"""
		if Agent.prompt_start == True:
			property_type = get_valid_input(
				"What type of property? ",
				("house", "apartment")).lower()
			payment_type = get_valid_input(
				"What payment type? ",
				("purchase", "rental")).lower()
			PropertyClass = self.type_map[
				(property_type, payment_type)]
			init_args = PropertyClass.prompt_init()
			self.property_list.append(PropertyClass(**init_args))
		else:
			print("Restart the program!")
			exit()
