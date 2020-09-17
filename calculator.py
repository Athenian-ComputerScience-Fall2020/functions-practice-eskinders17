'''
Collaborators: 

'''
def add(num1, num2):
   
   
   return num1 + num2

def substract(num1, num2):
   
   return num1 - num2

def multiply(num1, num2):
   
   return num1 * num2

def divide(num1, num2):
   
   return num1 % num2 
num1 = int(input("enter a number"))  
num2 = int(input("enter another number"))
x = int(input("press 1 to add, press 2 to substract, press 3 to multiply, press 4 to divise"))
if x == 1:
    print(add(num1, num2))
elif x == 2:
    print(substract(num1, num2))  
elif x == 3:
    print(multiply(num1, num2)) 
elif x == 4: 
    print(divide(num1, num2))
else:
    print("you put a wrong number") 
