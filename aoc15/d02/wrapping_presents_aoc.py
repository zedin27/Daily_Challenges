def wrapping_presents():
	# width, length, and height will have their respective values as an index 
	# 2*l*w + 2*w*h + 2*h*l ----> 2*value[0]*value[1]*value[2]
	# Have a way to parse the first numbers before "x" and add calculate it in a list
	# Have a way to parse the second numbers before "x" and add calculate it in a list
	# Have a way to parse the last couple digits after first and second are parsed and add calculate it in a list
	# e.g. length x width x height = 2 x 3 x 4 = 2(2x3) + 2(3x4) + 2(4x2)

	file_stream = open("input.txt", "r" )
	count = 0
	length = 0
	with file_stream as file:
		surface_areas = []
		ribbons = []
		for line in file:
			line = line.strip()
			dimensions = line.split('x')
			dimensions = [int(d) for d in dimensions]
			present_length = dimensions[0]
			present_width = dimensions[1]
			present_height = dimensions[2]
			perimeter = 2 * (present_length + present_width + present_height - max(present_length, present_width, present_height))
			bow = present_length * present_width * present_height
			lw = (dimensions[0] * dimensions[1])
			wh = (dimensions[1] * dimensions[2])
			hl = (dimensions[2] * dimensions[0])
			surface_area = lw + wh + hl
			minimum_side = min(lw, wh, hl)
			surface_areas.append(2 * (surface_area) + minimum_side)
			ribbons.append(perimeter + bow)

	# There are 1,000 elements in the list
	# Presents surface areas
	size = len(surface_areas)
	for x in range(size): 
		count += surface_areas[x]
	
	# Ribbons/bow
	size1 = len(ribbons)
	for x in range(size1): 
		length += ribbons[x]
	print(length)

wrapping_presents()