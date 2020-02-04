#Lesson 10 Project - RGB-HEX Converter
'''
RGB - HEX CONVERTER


In this project, we'll use Bitwise operators to build a calculator
that can convert RGB values to Hexadecimal (hex) values, and vice-versa.

We'll add three methods(=functions) to the project:
A method to convert RGB to Hex
A method to convert Hex to RGB
A method that starts the prompt cycle
The program should do the following:

INSTRUCTIONS:
1. Prompt the user for the type of conversion they want
2. Ask the user to input the RGB or Hex value
3. Use Bitwise operators and shifting in order to convert the value
4. Print the converted value to the user
It's useful to know some background on RGB and hex values, so we recommend reading the resources we linked to.

SPECIAL NOTES: As with professional software development,
               you should be saving your code very often.
               As you code, make sure you click the "Save" button below to save your code/changes.
               Otherwise, you run the risk of losing all your code.
'''
#1st Function (Method) = RGB TO HEX
def RGB_HEX():
    #message for prompting invalid input
    invalid_msg = "Invalid value entered"
    #we will take the values of the RGB from the user
    red = int(input("Enter R value: "))
    #validating the value from user
    if red < 0 or red > 255:
        print(invalid_msg)
        return
    green = int(input("Enter G value: "))
    if green < 0 or green > 255:
        print(invalid_msg)
        return
    blue = int(input("Enter B value: "))
    if blue < 0 or blue > 255:
        print(invalid_msg)
        return
    #Starting to work on the convertion of the values from RGB to HEX
    #storing our Hex value
    val = (red << 16) + (green << 8) + blue
    print(hex(val).upper())

def HEX_RGB():
    hex_val = input("Please enter a Hex value: ")
    #to convert HEX to RGB we need 24 bits for color
    #checking the length of the Hex value given - need to be 6 chars len
    if len(hex_val) != 6:
        print("Invalid value")
        return
    else:
        hex_val = int(hex_val, 16)

    #creating 2 hex digt variable to see how much of the color bits it ocuppies
    two_hex_digit = 2**8
    blue = hex_val % two_hex_digit
    hex_val = hex_val >> 8
    green = hex_val % two_hex_digit
    hex_val = hex_val >> 8
    red = hex_val % two_hex_digit
    print("RGB:(%s, %s, %s)" %(red, green, blue))

def convert():
    while True:
        option = input("Enter 1 to convert RGB to HEX.\n"
                       "Enter 2 to convert HEX to RGB.\n"
                       "Enter X to exit:")
        if option == "1":
            print("RGB to HEX..")
            RGB_HEX()
        elif option == "2":
            print("HEX to RGB...")
            HEX_RGB()
        elif option == "X" or option == "x":
            print("Exiting..")
            break
        else:
            print("Invalid message")
            try_again = input("Would you likt to try again (Y/N) ?")
            if try_again == "y" or try_again == "Y":
                continue
            elif try_again == "N" or try_again == "n":
                print("Exiting..")
                break


convert()





