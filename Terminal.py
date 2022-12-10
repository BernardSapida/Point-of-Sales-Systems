from account import Account
from inventory import Inventory


class Terminal:
  # This function prints a welcome message to the user.
  def __init__(self):
    print("WELCOME TO POINT-OF-SALES v2\n")

  # While True, display the menu
  # Creating an instance of the Account class & Inventory class.
  def start(self):
    # Facade Design
    self.account = Account()
    self.inventory = Inventory()

    while (True):
      self.displayMenu()

  """
  It displays a menu
  If user choose 1. Therefore, login function will be called
  If user choose 2. Therefore, signup function will be called
  If user choose 3. Therefore, there's no execution
  """
  def displayMenu(self):
    while (True):
      print("[1] Login")
      print("[2] Sign-up")
      print("[3] Exit")
      choice = input("Choice: ")

      if (choice == "1" or choice == "2" or choice == "3"): break
      print("Invalid input! Please try again.")
      print("\n====================================================================\n")
    print("\n====================================================================\n")

    if (choice == "1"):
      username = self.account.login()
      self.inventory.displayMenu(username)
    elif (choice == "2"):
      self.account.signUp()
