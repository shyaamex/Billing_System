from admin import admin
from consumer import buyer
# This is third file of the project which contains ""the peration class""
# and this operation class inherits ""buyer and admin class"" of previous files





# This operation class is used to descide whether you want to 
# perform admin operations or buyer operations 
 
class operation(buyer,admin):
    def __init__(self):
        super().__init__()
        pass
    
    def exe(self):
        print("""
        ____________________Convinience Store Portal________________________ 
    
            You are a :
            
                    1.) Admin 
                    2.) Buyer
        """)
        self.choice1=int(input())
        if self.choice1 == 1:
            username=input("Enter the username : ")
            password=input("Enter the password : ")
            if username == "shyam064" and password=="alpha99":
                self.instance1 = admin()
                self.instance1.menu()
            else:
                print("Username or password is invalid")
        elif self.choice1 == 2:
            self.instance2 = buyer()
            self.instance2.menu2()
        else:
            print("Enter a valid choice!!")
            self.exe()