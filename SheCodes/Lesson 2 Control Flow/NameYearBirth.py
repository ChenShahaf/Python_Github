def name_age():
	print("Please enter your birth year in 4 digits :")
	year_birth = int(input())
	print("Please enter your first name:")
	first_name = input()
	print("Please enter your last name: ")
	last_name = input()
	age = 2018 - year_birth
	intials = first_name[0] + last_name[0]
	print("Your intials are %s and you are %d old" % (intials, age))
	return None

name_age()


