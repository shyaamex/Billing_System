class user:
    def __init__(self):
        """         Constructor of class 'user'      """
        self.product = {0:['Parle-g','10'],1:['Hide & seek','40'],2:['Good day','20']}

  

class admin(user):
    """      Tasks of admin are written under admin class       """
    
    def display(self):
        print('\ncode    products')
        print("")
        for x,y in self.product.items():
            print(x,"   ",y)
        
    def menu(self):
        print("""
              Enter your choice : 
                1.) Add or replace a product
                2.) Remove a product
                3.) Modify a product
                4.) Show the list of products
                5.) Exit
              """)
        self.choice2 = int(input())
                    
        if self.choice2 == 1:
            self.add_product()
        elif self.choice2 == 2:
            self.remove_product()
        elif self.choice2 == 3:
            self.modify()
        elif self.choice2 == 4:
            print('\ncode    products')
            print("")
            for x,y in self.product.items():
                print(x,"   ",y)
            self.menu()
        elif self.choice2 == 5:
            print("Exited")
            exit
        
    def add_product(self):
        print('code    product')
        print("")
        for x,y in self.product.items():
            print(x,"   ",y)
            
        self.prod_code=int(input("Enter the product code that your want to replace or you want to add : "))
        self.prod_details=list()
        i=0
        while(i<2):
            ant=['Name','Price']
            self.prod_details.append(input(f"Enter the <<< { ant[i] } >>> of the product:"))
            i+=1
        self.product[self.prod_code]=self.prod_details
        print("Proudct Successfully added/replaced ")
        self.menu()
    
    
    def remove_product(self):
        
        
        print('code    product')
        print("")
        for x,y in self.product.items():
            print(x,"   ",y)
            
            
        print("Enter the product code of the product that you want to remove : ")
        self.prod_code=int(input())
        print(self.product[self.prod_code]," has been removed ")
        del self.product[self.prod_code]
        self.menu()
    
    def modify(self):
        
        
        print('code    product')
        print("")
        for x,y in self.product.items():
            print(x,"   ",y)
            
            
        print("Enter the product code of the product that you want to modify : ")
        print("""
              Enter your choice :
                    1.) You want to modify product name
                    2.) You want to modify product price
                    3.) Exit
              """)
        self.choice3 = int(input())
        
        if self.choice3 ==1:
            print("Enter the product code of the product : ")
            self.prod_code=int(input())
            self.newname=input("Enter the name you want to add : ")
            self.product[self.prod_code][0]=self.newname
            self.menu()
            
        elif self.choice3 ==2:
            
            print("Enter the product code of the product : ")
            prod_code=int(input())
            newprice=input("Enter the price you want to add : ")
            self.product[prod_code][1]=newprice
            self.menu()
            
        elif self.choice3 ==3:
            print("Exited...")
            self.menu()
        else:
            print("Enter a valid choice ")
            self.modify()
           