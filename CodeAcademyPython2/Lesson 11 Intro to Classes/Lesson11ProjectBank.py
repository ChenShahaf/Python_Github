#Lesson 11 - Bank Account
'''
In this project, we'll create a Python class that can be used to create and manipulate a personal bank account.

The bank account class you'll create should have methods for each of the following:
1. Accepting deposits
2. Allowing withdrawals
3. Showing the balance
4. Showing the details of the account

SPECIAL NOTES: As with professional software development, you should be saving your code very often.
               As you code, make sure you click the "Save" button below to save your code/changes.
               Otherwise, you run the risk of losing all your code!
'''
class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    '''
     REPR = method defines what represents the object when a user tries to print that object using print.
     Let's add to this method and make it descriptive.
     '''
    return ("%s's account. Balance: $%.2f" %(self.name, self.balance))
  def show_balance(self):
    print("Total balance is: $%.2f" %(self.balance))
  def deposit(self, amount):
    #checking for errors
    if amount <= 0 :
      print("ERROR - Deposite needs to be a positive amoount")
      return
    else:
      print("The amount deposited into the account is: $%.2f" %(amount))
      self.balance += amount
      self.show_balance()
  def withdraw(self, amount):
    #checking for errors
    if amount > self.balance:
      print("Not enough money in account")
      return
    else:
      print("Withdrawn $%.2f" %(amount))
      self.balance -= amount
      self.show_balance()

my_account = BankAccount("Matt")
print(my_account)
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print(my_account)



