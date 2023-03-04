from admin import admin
# This is the second file of this project which contains "the buyer class" 
# and this buyer class inherits "" the admin class "" from previous file





# Operations of  buyer are defined in this buyer class
class buyer(admin):
       
       
       
       # This method displays menu to the user and revcieves the product code and send it to "buy method"
       def menu2(self):
           print("""
                 Choose the products that you want to purchase
                 """)
           self.instance23= admin()
           self.instance23.display()
           print("\n Enter product code of your choice : ")           

           self.prod_code=int(input())
           self.buy()
       
       
       
       # This accepts the product code from "" menu2 method "" and returns the name of product 
       # which you want to buy and returns its price
       def buy(self):
            
            print(f"Product you want to purchase is :  { self.product[self.prod_code][0] } ")
            print("\n\n")
            price = int(self.product[self.prod_code][1])
            print(f"You have to pay ₹ { price } ")
