
from admin import user,admin

class buyer(admin):
       
       def menu2(self):
           print("""
                 Choose products that you want to buy
                 """)
           self.instance23= admin()
           self.instance23.display()
           print("\n Enter product code of your choice : ")           

           self.prod_code=int(input())
           self.buy()
       
       def buy(self):
            
            print(f"Product you want to purchase is :  { self.product[self.prod_code][0] } ")
            print("\n\n")
            price = int(self.product[self.prod_code][1])
            print(f"You have to pay ₹ { price } ")