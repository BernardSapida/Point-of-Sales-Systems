class Account:
    """
    It creates a list of dictionaries, each dictionary containing a username, fullname, role, and
    password
    """
    def __init__(self):
        self.accounts = [
            {
                "Username": "Admin",
                "Fullname": "Administrator",
                "Role": "ADMIN",
                "Password": "admin123"
            }
        ]

    # It asks for a username and password
    def login(self):
        while(True):
            print("LOGIN POS v2\n")
            print("To login, enter your username and password:\n")
            username = input("Username: ")
            password = input("Password: ")

            # if the username and password are valid, it returns the username.
            if(self.validCredential(username, password)):
                print("\n====================================================================\n")
                return username
            print("Invalid login credentials. Forgot your password? contact your admin.")
            print("\n====================================================================\n")

       
    # It creates an account
    def signUp(self):
        print("CREATE AN ACCOUNT\n")
        username = input("Username: ")
        fullname = input("Full Name: ")
        role = input("Role (ADMIN/CASHIER): ")
        
        # A loop that will keep asking for the role until the user enters either ADMIN or CASHIER.
        while(True):
            if(role == "ADMIN" or role == "CASHIER"): break
            print("Role should be ADMIN or CASHIER! Please try again.")
            print("\n====================================================================\n")
            role = input("Role (ADMIN/CASHIER): ")

        password = input("Password: ")
        confirmPassword = input("Re-type Password: ")

        # A loop that will keep asking for the password until the user enters the same password.
        while(True):
            if(password == confirmPassword): break
            print("Password and Confirm Password didn't matched! Please try again.")
            print("\n====================================================================\n")
            confirmPassword = input("Re-type Password: ")

        # It adds a new account to the list of accounts.
        self.accounts.append({
            "Username": username,
            "Fullname": fullname,
            "Role": role,
            "Password": password
        })

        print("\nYour account has been created. You may now login.")
        print("\n====================================================================\n")
    
    """
    It checks if the username and password are in the accounts list
    
    :param username: The username of the account
    :param password: The password of the account
    :return: a boolean value.
    """
    def validCredential(self, username, password):
        for account in self.accounts:
            if(account["Username"] == username and account["Password"] == password):
                return True
        return False