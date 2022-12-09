import random

class Inventory:
    # It initializes the class with a subTotal of 0, and a list of dictionaries called inventory.
    def __init__(self):
        self.subTotal = 0
        self.CODE_MAX_LENGTH = 10
        self.NAME_MAX_LENGTH = 23
        self.BRAND_MAX_LENGTH = 17
        self.UNIT_MAX_LENGTH = 10
        self.PRICE_MAX_LENGTH = 10
        self.inventory = [
            {
                "Code": "00001",
                "Name": "Bear Brand",
                "Brand": "Nestle",
                "Unit": "10",
                "Price": "15"
            },
            {
                "Code": "00002",
                "Name": "Pancit Canton",
                "Brand": "Lucky Me",
                "Unit": "10",
                "Price": "20"
            },
            {
                "Code": "00003",
                "Name": "Coke",
                "Brand": "Coca Cola",
                "Unit": "20",
                "Price": "30"
            },
            {
                "Code": "00004",
                "Name": "Dishwashing Liquid",
                "Brand": "Joy",
                "Unit": "15",
                "Price": "12"
            },
            {
                "Code": "00005",
                "Name": "Shampoo",
                "Brand": "Pantene",
                "Unit": "5",
                "Price": "8"
            },
            {
                "Code": "00006",
                "Name": "Sardines",
                "Brand": "Ligo",
                "Unit": "25",
                "Price": "22"
            },
            {
                "Code": "00007",
                "Name": "Meatloaf",
                "Brand": "Argentina",
                "Unit": "10",
                "Price": "25"
            },
            {
                "Code": "00008",
                "Name": "Cornbeek",
                "Brand": "CDO",
                "Unit": "10",
                "Price": "25"
            },
            {
                "Code": "00009",
                "Name": "Hotdog",
                "Brand": "Tender Juicy",
                "Unit": "10",
                "Price": "25"
            },
            {
                "Code": "00010",
                "Name": "Nescafe Pack",
                "Brand": "Nestle",
                "Unit": "20",
                "Price": "8"
            }
        ]

    # It displays a menu for the user to choose from.
    def displayMenu(self, username):
        while(True):
            print(f"Welcome, {username}!\n")
            print("[1] New Customer")
            print("[2] Inventory")
            print("[3] Logout")
            choice = input("Choice: ");

            
            # If choice is equal to 1 the makeOrder() and displayPayment() functions.
            if(choice == "1"):
                self.makeOrder()
                self.displayPayment()

            # If choice is equal to 2 the displayInventory() and displayOptions() functions.
            elif(choice == "2"):
                self.displayInventory()
                self.displayOptions()
            
            # If choice is equal to 3 the while loop will terminate.
            elif(choice == "3"): break

            # If choice is not 1, 2, or 3. The input is invalid and will ask again.
            else:
                print("Invalid input! Please try again.")
                print("\n====================================================================\n")
        print("\n====================================================================\n")

    # It prints out the inventory (List of products).
    def displayInventory(self):
        print(
            "CODE" + " "*(self.CODE_MAX_LENGTH - 4) + 
            "NAME" + " "*(self.NAME_MAX_LENGTH - 4) + 
            "BRAND" + " "*(self.BRAND_MAX_LENGTH - 5) + 
            "UNIT" + " "*(self.UNIT_MAX_LENGTH - 4) + 
            "PRICE" + " "*(self.PRICE_MAX_LENGTH - 5)
        )

        for product in self.inventory:
            print(
            product["Code"] + " "*(self.CODE_MAX_LENGTH - len(product["Code"])) + 
            product["Name"] + " "*(self.NAME_MAX_LENGTH - len(product["Name"])) + 
            product["Brand"] + " "*(self.BRAND_MAX_LENGTH - len(product["Brand"])) + 
            product["Unit"] + " "*(self.UNIT_MAX_LENGTH - len(product["Unit"])) + 
            product["Price"]+ " "*(self.PRICE_MAX_LENGTH - len(product["Price"]))
        )

        print("\n====================================================================\n")

    """
    It displays the options for the user to choose from, and then calls the addProduct() function if
    the user chooses to add a product.
    """
    def displayOptions(self):
        # A while loop that will keep on looping until the user enters 1 or 2.
        while(True):
            print("Options:\n")
            print("[1] Add Product")
            print("[2] Back")
            choice = input("Choice: ");

            if(choice == "1" or choice == "2"): break
            print("Invalid input! Please try again.")
            print("\n====================================================================\n")
        print("\n====================================================================\n")

        # Calling the addProduct() function if the user chooses to add a product.
        if(choice == "1"): self.addProduct();

    # It adds a new product to the inventory.
    def addProduct(self):
        while(True):
            print("ADD NEW PRODUCT\n")
            code = input("Product Code: ")
            # It checks if the product code already exists. 
            # If it does, it will ask the user to input a new product code.
            while(True):
                if(not self.isProductCodeExist(code)): break
                print("Product code already exists! Please try again.")
                print("\n====================================================================\n")
                code = input("Product Code: ")

            name = input("Product Name: ")
            brand = input("Brand Name: ")
            unit = input("Unit: ")
            price = input("Price (PHP): ")

            # It adds a new product to the inventory.
            self.inventory.append(
                {
                    "Code": code,
                    "Name": name,
                    "Brand": brand,
                    "Unit": unit,
                    "Price": price
                }
            )

            print("New product was added to inventory.")
            print("\n====================================================================\n")
            response = input("Do you want to add another product (y/n): ")
            print("\n====================================================================\n")

            if(response == "n"): break

    """
    It displays the inventory, then asks the user to enter a product code. 
    If the user enters a product code, it reduces the product unit by 1. 
    If the user enters nothing, it breaks the loop.
    """
    def makeOrder(self):
        print("NEW ORDER\n")
        print("ITEMS IN CART\n")

        # It displays the inventory, then asks the user to enter a product code. 
        self.displayInventory()

        while(True):
            productCode = input("ENTER CODE: ")

            # If the user enters nothing, it breaks the loop.
            if(productCode == ""): break

            # If the user enters a product code, it reduces the product unit by 1. 
            self.reduceProductUnit(productCode)
            print("\n====================================================================\n")
    
    """
    It asks the user to input a payment
    If the payment is less than the subTotal 
    It will ask the user to input a payment again
    """
    def displayPayment(self):
        print("\n====================================================================\n")
        print(f"SUB-TOTAL: {self.subTotal}")

        # Asking the user to input a payment. 
        #  If the payment is less than the subTotal
        # It will ask the user to input a payment again.
        while(True):
            payment = int(input("Payment: "))
            if(payment >= self.subTotal): break
            print("Insufficient funds! Please try again.")
            print("\n====================================================================\n")
            
        # Printing the change.
        print(f"Change: {payment - self.subTotal}\n")

        # Printing the receipt number.
        print(f"TRANSACTION COMPLETE: RECEIPT NO. {random.randrange(10000000, 99999999)}\n")

        self.subTotal = 0

        input("[Press ENTER to continue]")
        print("\n====================================================================\n")

    """
    It takes a product code as an argument, and if the product code is found in the inventory, it
    reduces the unit by 1 and adds the price of the product to the subtotal
    """
    def reduceProductUnit(self, productCode):
        found = False

        for i in range(0, len(self.inventory)):
            # Checking if the product code is found in the inventory.
            # If it is found, it reduces the unit by 1 and
            # adds the price of the product to the subtotal.
            if(self.inventory[i]["Code"] == productCode):
                found = True

                # It checks if the product unit is not equal to 0. If it is not equal to 0, 
                # it reduces the product unit by 1 and adds the product price to the subTotal.
                if(self.inventory[i]["Unit"] != "0"):
                    self.inventory[i]["Unit"] = str(int(self.inventory[i]["Unit"]) - 1)
                    self.subTotal += int(self.inventory[i]["Price"])
                    print(self.inventory[i]["Name"] + " Added to Cart!")
                # It checks if the product unit is equal to 0. If it is equal to 0, 
                # it prints out the product is out of stock.
                else:
                    print(self.inventory[i]["Name"] + " is out of stock!")
        
        # It checks if the product code is not found in the inventory.
        # If it is not found, it prints out the product code not found.
        if(not found): print(productCode + " not found!")

    # It checks if the product code exists in the inventory
    def isProductCodeExist(self, productCode):
        # It checks if the product code exists in the inventory.
        for product in self.inventory:
            if(product["Code"] == productCode): return True
        return False