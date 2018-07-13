"""Classes for melon orders."""

class AbstractMelonOrder:

	# included attributes for both domestic and international melon orders
	def __init__(self,species, qty):
		"""Initialize abstract melon order attributes"""
		self.species = species
		self.qty = qty
		self.shipped = False


	def get_total(self):
		"""Calculate price, including tax."""

		base_price = 5
		total = (1 + self.tax) * self.qty * base_price

		return total

	def mark_shipped(self):
		"""Record the fact than an order has been shipped."""

		self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
	"""A melon order within the USA."""

	# class attributes
	order_type = "domestic"
	tax = 0.08
	# didn't need to have dunder init here because nothing changed from the parent class


class InternationalMelonOrder(AbstractMelonOrder):
	"""An international (non-US) melon order."""

	order_type = "international"
	tax = 0.17

	# wrote dunder init because for every instance of class InternationalMelonOrder we need a country code
	def __init__(self, species, qty, country_code):
		"""Initialize melon order attributes."""
		
		# calling the parent class with the super fx to obtain self, species, and qty
		super().__init__(species, qty)

		self.country_code = country_code

	def get_country_code(self):
		"""Return the country code."""

		return self.country_code
