#LESSON 11 INTRO TO CLASSES
def PART1():
    '''
    PART 1 OF 18 - Why Use Classes?

    Python is an object-oriented programming language,
    which means it manipulates programming constructs called objects.
    You can think of an object as a single data structure that contains data as well as functions;
    the functions of an object are called its methods.

    For example: any time you call
                len ("Eric")
                Python is checking to see whether the string object you passed it has a length,
                and if it does, it returns the value associated with that attribute.
    Example 2: When you call
               my_dict.items()
               Python checks to see if my_dict has an items() method (which all dictionaries have)
               and executes that method if it finds it.

    But what makes "Eric" a string and my_dict a dictionary?
    The fact that they're instances of the str and dict classes,
    respectively.

    A CLASS = is just a way of organizing and producing objects with similar attributes and methods.
    '''
    print("Part 1 of 18:")
    '''
    In this part We've defined our own class, Fruit, and created a lemon instance.
    run the code and get started creating classes and objects of your own.
    '''
    class Fruit(object):
        """A class that makes various tasty fruits."""
        def __init__(self, name, color, flavor, poisonous):
            self.name = name
            self.color = color
            self.flavor = flavor
            self.poisonous = poisonous
            self.is_edible = self.is_edible()

        def description(self):
            print ("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))
        def is_edible(self):
            if not self.poisonous:
                print("Yep! I'm edible.")
            else:
                print("Don't eat me! I am super poisonous.")

    lemon = Fruit("lemon", "yellow", "sour", False)

    lemon.description()
    lemon.is_edible()

def PART2To6():
    '''
    PART 2 OF 18 - Class Syntax

    A basic class consists only of the class keyword, the name of the class,
    and the class from which the new class inherits in parentheses.
    (We'll get to inheritance soon.)

    For now, our classes will inherit from the object class, like so:
    class NewClass(object):
        #Class magic here

    This gives them the powers and abilities of a Python object.
    By convention, user-defined Python class names start with a capital letter.

    1. INSTRUCTION - Create a class called Animal.
    2. DEFINING THE CLASS - 1.  __init__().
    3. INSTATIATE (create) our first object.
    4.


    '''
    print("Part 2-6 of 18:")
    class Animal(object):
        '''
        class definition off with an odd-looking function:
          This function is required for classes,
                                and it's used to initialize the objects it creates.
                                __init__() always takes at least one argument,
                                self, that refers to the object being created.
                                You can think of __init__()
                                as the function that "boots up" each object the class creates.
        '''
        #initialize the class
        def __init__(self, name, age, is_hungry):
            '''
            EXPLAINATION ABOUT SELF

             SELF= This is a Python convention; there's nothing magic about the word self.
                    However, it's overwhelmingly common to use self as the first parameter in __init__(),
                    so you should do this so that other people will understand your code.

             The part that is magic is the fact that self is the first parameter passed to __init__().
             Python will use the first parameter that __init__() receives to refer to the object being created;
             this is why it's often called self, since this parameter gives the object being created its identity.
            '''
            """Makes cute animals."""
            self.name = name
            self.age = age
            self.is_hungry = is_hungry
            pass
            '''
            We can access attributes of our objects using dot notation. Here's how it works:
            EXAMPLE 
            
            class Square(object):
                    def __init__(self):
                        self.sides = 4
            
            my_shape =Square()
            print (my_shape.sides)        
            
            1. we created a class named square, with the attribute sides
            2. Outside the class definition, 
               we create a new instance of Square named my_shape and access that attribute using my_shape.sides.
            '''
            #Part 5 of 18 - creating zebra named Jeffery

def PART7():
    print("Part 7- of 18:")
    class Animal(object):
        is_alive = True
        def __init__(self, name, age):
        #Makes cute animals.
            self.name = name
            self.age = age
            pass
    # Note that self is only used in the __init__()
    # function definition; we don't need to pass it
    # to our instance objects.
    zebra = Animal("Jeffrey", 2)
    giraffe = Animal("Bruce", 1)
    panda = Animal("Chad", 7)
    #PART 7 - Class Scope
    '''
    The scope of a variable is the context in which it's visible to the program.
    
    When dealing with classes, you can have variables that are available everywhere (global variables), 
    variables that are only available to members of a certain class (member variables), 
    and variables that are only available to particular instances of a class (instance variables).
    
    The same goes for functions: some are available everywhere,
     some are only available to members of a certain class, 
     and still others are only available to particular instance objects.
     
    Check out the code in the editor. 
    Note that each individual animal gets its own name and age (since they're all initialized individually), 
    but they all have access to the member variable is_alive, 
    since they're all members of the Animal class. Click Run to see the output!
    '''
    print(zebra.name, zebra.age, zebra.is_alive)
    print(giraffe.name, giraffe.age, giraffe.is_alive)
    print(panda.name, panda.age, panda.is_alive)

def PART8():
    print("Part 8 of 18:")
    '''

    INSTRUCTIONS - Add a method, description, to your Animal class.
    SPECIAL NOTES
    1. Using two separate print statements,
    2. it should print out the name and age of the animal it's called on.
    3. Then, create an instance of Animal, hippo (with whatever name and age you like),
        and call its description method.

    '''
    class Animal(object):
        """Makes cute animals."""
        is_alive = True
        def __init__(self, name, age):
            self.name = name
            self.age = age
        # Add your method here!
        def description(self):
            print(self.name)
            print(self.age)

    hippo = Animal("Anderson", 36)
    hippo.description()

def PART9():
    print("Part 9 of 18:")
    class Animal(object):
        """Makes cute animals."""
        is_alive = True
        health = "good"
        def __init__(self, name, age):
            self.name = name
            self.age = age
        # Add your method here!
        def description(self):
            print(self.name, end=" ")
            print(self.age, end=" ")
            print(self.health, end=" \n")

    hippo = Animal("Anderson", 36)
    sloth = Animal("Fluffy", 10)
    ocelot = Animal("Kitty", 1)

    hippo.description()
    sloth.description()
    ocelot.description()

def PART10():
    print("Part 10 of 18: ")
    '''
    Classes like Animal and Fruit make it easy to understand the concepts of classes and instances, 
    but you probably won't see many zebras or lemons in real-world programs.
    However, classes and objects are often used to model real-world objects. 
    The code in the editor is a more realistic demonstration of the kind of classes and objects you might find 
    in commercial software. 
    
    Here we have a basic ShoppingCart class for creating shopping cart objects for website customers; 
    though basic, it's similar to what you'd see in a real program.
    '''
    class ShoppingCart(object):
        """Creates shopping cart objects
        for users of our fine website."""
        items_in_cart = {}
        def __init__(self, customer_name):
            self.customer_name = customer_name

        def add_item(self, product, price):
            """Add product to the cart."""
            self.product = product
            if not product in self.items_in_cart:
                self.items_in_cart[product] = price
                print(product + " Added")
            else:
                print(product + " is already in the cart.")

        def remove_item(self, product):
            """Remove product from the cart."""
            if product in self.items_in_cart:
                del self.items_in_cart[product]
                print(product + " removed.")

            else:
                print(product + " is not in the cart.")
    my_cart = ShoppingCart("Chen")
    my_cart.add_item("Sugar", 12)

def PART11():
    print("Part 11 of 18 - Inheritance.")
    #Part 11 - Inheritance
    '''
    Inheritance is a tricky concept, so let's go through it step by step.

    Inheritance = is the process by which one class takes on the attributes and methods of another,
                  and it's used to express an is-a relationship.

    For example:
    a Panda is a bear, so a Panda class could inherit from a Bear class.
    However, a Toyota is not a Tractor, so it shouldn't inherit from the Tractor class
    (even if they have a lot of attributes and methods in common).
    Instead, both Toyota and Tractor could ultimately inherit from the same Vehicle class.
    '''

    class Customer(object):
        """Produces objects that represent customers."""

        def __init__(self, customer_id):
            self.customer_id = customer_id

        def display_cart(self):
            print("I'm a string that stands in for the contents of your shopping cart!")


    class ReturningCustomer(Customer):
        """For customers of the repeat variety."""

        def display_order_history(self):
            print("I'm a string that stands in for your order history!")


    monty_python = ReturningCustomer("ID: 12345")
    monty_python.display_cart()
    monty_python.display_order_history()

def PART12():
    print("Part 12 of 18 - Inheritance Syntax.")
    #PART 12  - Inheritance Syntax
    '''
    In Python, inheritance works like this:
    ======================================
    =   class DerivedClass(BaseClass):   =
    =   #Enter code in here              =
    ======================================
    DerivedClass  = the new class you're making 
    BaseClass  = the class from which that new class inherits.
    '''
    class Shape(object):
        """Makes shapes!"""

        def __init__(self, number_of_sides):
            self.number_of_sides = number_of_sides

    # Add your Triangle class below!
    class Triangle(Shape):
        def __init__(self, side1, side2, side3):
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3

def PART13():
    print("Part 13 of 18: Override!")
    '''
    Sometimes you'll want one class that inherits from another
     to not only take on the methods and attributes of its parent, but to override one or more of them.
     
     EXAMPLE:
     class Employee(object):
        def __init__(self, name):
            self.name = name
            def greet(self, other):
                print("Hello %s" %(other.name))
    class CEO(Employee):
        def greet(self, other):
            print("Get back to work, %s!" %(other.name))
    ceo = CEO("Emily")
    emp = Employee("Steve")
    emp.greet(ceo)
    # Hello, Emily
    ceo.greet(emp)
    # Get back to work, Steve!        
     
     OVERRIDE = RE-CREATE INHIRATE METHOD
     
     Rather than have a separate greet_underling method for our CEO, 
     we override (or re-create) the greet method on top of the base Employee.greet method. 
     This way, we don't need to know what type of Employee we have before we greet another Employee.           
    '''
    class Employee(object):
        """Models real-life employees!"""
        def __init__(self, employee_name):
            self.employee_name = employee_name

        def calculate_wage(self, hours):
            self.hours = hours
            return hours * 20.00
    # Add your code below!
    '''
    Create a new class, PartTimeEmployee, that inherits from Employee.
    '''
    class PartTimeEmployee(Employee):
        '''
        Give your derived class a calculate_wage method that overrides Employee's.
        It should take self and hours as arguments.
        '''
        def calculate_wage(self, hours):
            '''
            Because PartTimeEmployee.calculate_wage overrides Employee.calculate_wage,
            it still needs to set self.hours = hours.
            '''
            self.hours = hours
            '''
            It should return the part-time employee's number of hours worked multiplied by 12.00 
            (that is, they get $12.00 per hour instead of $20.00).
            '''
            return hours * 12.00

def PART14():
    #PART 14 PF 18 - This Looks Like a Job For...
    '''
    On the flip side, sometimes you'll be working with a derived class (or subclass)
    and realize that you've overwritten a method or attribute defined in that class' base class
    (also called a parent or superclass) that you actually need.
    Have no fear! You can directly access the attributes or methods of a superclass with Python's built-in super call.

    SYNTAX FOR CALLING SUPER CLASS:
    =============================================
    =   class Derived(Base):                    =
    =       def m(self):                        =
    =           return super(Derived, self).m() =
    =============================================
    m() = method from the base class.
    '''
    class Employee(object):
        """Models real-life employees!"""

        def __init__(self, employee_name):
            self.employee_name = employee_name

        def calculate_wage(self, hours):
            self.hours = hours
            return hours * 20.00

    # Add your code below!
    class PartTimeEmployee(Employee):
        def calculate_wage(self, hours):
            self.hours = hours
            return hours * 12.00
        def full_time_wage(self, hours):
            return super(PartTimeEmployee, self).calculate_wage(hours)

    milton = PartTimeEmployee("Milton")
    print(milton.full_time_wage(10))

def PART15to18():
    #Class Basics
    '''
    Create a class:
    1. Triangle. Its __init__() method should take self, angle1, angle2, and angle3 as arguments.
    Make sure to set these appropriately in the body of the __init__() method (see the Hint for more).
    '''
    class Triangle(object):
        number_of_sides = 3
        def __init__(self, angle1, angle2, angle3):
            self.angle1 = angle1
            self.angle2 = angle2
            self.angle3 = angle3
        def check_angles(self):
            if(self.angle1 + self.angle2 + self.angle3) == 180:
                return True
            else:
                return False
    class Equilateral(Triangle):
        angle = 60
        def __init__(self):
            self.angle1 = self.angle
            self.angle = self.angle
            self.angle3 = self.angle

    my_triangle = Triangle(90, 30, 60)
    print(my_triangle.number_of_sides)
    print(my_triangle.check_angles())







PART15to18()