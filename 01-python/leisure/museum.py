def draw_museum(height = 3):
	"""
	Draw a museum with specified height.

	Parameters:
	height(int): the height of the pillars of the museum.

	Returns:
	None

	"""

	print("   ==============")
	print("  =              =")
	print(" =                = ")
	print("=                  =")
	print("====================")
	for _ in range(height):
		print("|| || || || || || ||")
	print("====================")
	return
