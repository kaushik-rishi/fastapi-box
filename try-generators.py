def custom_range(i):
	index = 0
	print("before entering while loop", end="\n\n")

	while index < i:
		print(f"while loop: {index}")

		if index % 2 == 0:
			yield index

		index += 1

	print(f"function exit being called @ index {index}")

cr = custom_range(10)
for i in cr:
	print("printing i: ", i)