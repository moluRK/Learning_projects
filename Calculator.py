# TO perform all basic arthimatic operations
print("""write "stop" in operation to stop program or "operations" to continue""")
import math
while True:
    class Calculator:
        def add(self,a,b):      
            return a+b
        def subs(self,a,b):     
            return a-b
        def multiply(self,a,b): 
            return a*b
        def divide(self,a,b):   
            # if b!=0:
            return a/b if b!=0 else print ("Error! division by zero is not defined.")
        def squareroot(self,a):  
            return math.sqrt(a) if a>0 else print("squareroot of negative number cannot be found. ")
        def power(self,a,b):     
            return a**b
        def percentage(self,a,b): 
            return a/100*b
    calc=Calculator()      
    a=float(input("Enter 1st number: "))
    op=input("""Enter operator:" "+","-","*","/","**"sqrt,%: """) 
    if op in ["+","-","*","/","**","%"] :         
        b=float(input("Enter 2nd number: "))# Ask for 2nd number only if operation need 
    if op == "+":
        print(f"{a} + {b} = {calc.add(a,b)}")
    elif op =="-":
        print(f"{a} - {b} = {calc.subs(a,b)}")
    elif op =="*":
        print(f"{a} x {b} = {calc.multiply(a,b)}")
    elif op =="/":
        print(f"{a} / {b} = {calc.divide(a,b)}")
    elif op =="sqrt":
        print(f"squareroot of {a} is {calc.squareroot(a)}")
    elif op =="**":
        print(f" ({a})^{b} is {calc.power(a,b)}")
    elif op == "%":
        print(f'{b} percent of {a} = {calc.percentage(a,b)}')
    elif op=="stop":
        break
    else :
        print("Invalid operator ,please GOOGLE it")