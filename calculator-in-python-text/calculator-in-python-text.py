print("Welcome to the calculator program in Python made with Aniket Sundriyal")

num1= float(input("Enter first number: "))
num2= float(input("Enter second number: "))

print("select the operation:")
print("1.ADD")
print("2.subtract")
print("3.multiply")
print("4.divided")

choice= input("enter your choice (1/2/3/4):")

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x * y
def divided (x,y):
    if y==0:
        return"Error! Division by zero"
    return x/y

if choice=='1':
    print ("result:",add(num1,num2))
elif choice=='2':
    print ("result:",subtract(num1,num2))
elif choice=='3':
    print("result:",multiply(num1,num2))
elif choice =='4':
   print("result:",divided(num1,num2))
else:
    print ("invaild input")


          
          
