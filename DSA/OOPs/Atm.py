# Creating miniproject to depict working of an ATM

class Atm:
    def __init__(self):
        # We need Atm pin and customer balance of the user
        pin=""
        balance = 0
        # Calling menu function
        self.menu()
    
    
    #Creating a menu function which will be display on the screen all the time.
    def menu(self):
        
        print("""
            Hello, How can I help you?
            1. Press 1 to create pin
            2. Press 2 to check balance
            3. Press 3 to withdraw
            4  Press 4 to change pin
            5. Press any button to exit !
            
            """)
        choice = input("Enter your choice : ")
        
       # Based on user choice we have to implement functionality
        if choice=='1':
            # To create pin
          self.createPin()
            
        # elif choice == '2' :
            
        # elif choice == '3' :
            
        # elif choice == '4' :
        
        
        # else:
        # print("Thank you  for banking with us ! have a great day !!")
        # exit() 
              
    def createPin(self):
        # Due to lack of database function right now we will ask user for Atm pin and balance for the first time
        pin = input("Enter 4 digit pin you want to set for your account: ")
        
        if len(pin) != 4:
            print(f"Its {len(pin)} digit now. Please enter 4 digit pin !!!")
            self.createPin()
        
        self.pin=pin
        # To set balance of first customer
        self.setBalance()
        print("Your pin has been created successfully !")
        # To shoe menu again
        self.menu()
        
    def setBalance(self):
        balance = input("Please enter your account balanace : ")
           # To check enter balance is numeric value or not 
        if  not balance.isnumeric():
            print("Enter Numeric(0-9) value only.")
            self.setBalance()
        self.balance = balance
        return balance

# Creating Atm object 
Atm()