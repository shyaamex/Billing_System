# This is the first file of the project which contains ""User class"" and ""admin class""



class user:
    def __init__(self):
        """         Constructor of class 'user'      """
        # List of products, Key of this dictionary would be the product code and value 
        # of those keys would be name and price [name, price]
        
        self.product = {0:['Parle-g','10'],1:['Hide & seek','40'],2:['Good day','20']}

  




# Operations of  admin are defined in this admin class

class admin(user):
    """      Tasks of admin are written under admin class       """
    
    
    
    
    
    
    # This method displays the list of all proudcts
    def display(self):
        print('\ncode    products')
        print("")
        for x,y in self.product.items():
            print(x,"   ",y)
    
    
    
    
    
    
    # This method shows choice of operation that can be performed with admin
    # It accepts the choices from users and assign new methods to them to perform
    # those choice as actions.
       
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
     
     
     
     
     # This method accepts choice from ""menu method""  
     # and add a new product to the list of products  
     
      
    def add_product(self):
        self.display()
            
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
    
    
    
    # This method accepts choice from ""menu method"" 
    # This method removes products from the list
    
    def remove_product(self):
        self.display()
            
            
        print("Enter the product code of the product that you want to remove : ")
        self.prod_code=int(input())
        print(self.product[self.prod_code]," has been removed ")
        del self.product[self.prod_code]
        self.menu()
    
    
    
    
    # This method accepts choice from ""menu method"" 
    # and it can modify the name or price of listed product
    # as pe your requirement.
    
    def modify(self):
        
        self.display()            
            
        print("Enter the product code of the product that you want to modify : ")
        print("""
              Enter your choice :
                    1.) You want to modify product name
                    2.) You want to modify product price
                    3.) Exit
              """)
        self.choice3 = int(input())
        
        
        # The code written below takes the existing product form list 
        # and it alters the name of that product.
        
        if self.choice3 ==1:
            print("Enter the product code of the product : ")
            self.prod_code=int(input())
            self.newname=input("Enter the name you want to add : ")
            self.product[self.prod_code][0]=self.newname
            self.menu()
         
         
        # The code written below takes the existing product form list 
        # and it alters the price of that product.   
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
           