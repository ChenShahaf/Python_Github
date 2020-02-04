def name_age ():
        print ("Please enter your birth year in 4 digits :")
        year_birth = int(input())
        if type(year_birth) == int:
                print ("Please enter your first name:")
                first_name = input()
                print ("Please enter your last name: ")
                last_name = input()
                age = 2018 - year_birth
                initials = first_name[0] + last_name[0]
                initials = initials.upper()
                print ("Your initials are %s and your age is %d" % (initials, age))
        else:
                print("Invalid input")
        return None
name_age()
