from add  import add
from sub import sub

num1= int(input("Enter no.1:"))
num2 = int(input("Enter no.2:"))


choice = int(input('''Enter the choice:
        1. Add
         2.Subtract'''))
if choice==1:
	add(num1,num2)\n",
        print(\"Addition is:\", add(num1,num2))
elif choice==2:
	sub(num1,num2)\n",
        print(\"Subtraction is:\", sub(num1,num2))
