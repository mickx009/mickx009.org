import random
import pprint

# Tuple
suits = ('hearts', 'diamonds', 'clubs', 'spades')

# Range
values = range(1, 14)

# List
cards = []

# For loop appending empty cards list with suits tuple and values range
for s in suits:
	for v in values:
		cards.append("{0} of {1}".format(v, s))

print(random.choice(cards))




