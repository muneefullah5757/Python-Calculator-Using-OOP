class calculator:
    def __init__(self,value1,value2):
        self.val1=value1
        self.val2=value2
    def add(self):
            return self.val1+self.val2
    def sub(self):
            return self.val1-self.val2
    def mul(self):
            return self.val1*self.val2
    def div(self):
            if self.val2==0:
                return 'Division by zero error'
            else:
                return self.val1/self.val2
    def str(self):
        return f"Calculator with values {self.val1} and {self.val2}" 
    def bool(self):
        return self.val1!=0 and self.val2!=0
while True:  
  print("Welcome to the calculator program!")
  print("CALCULATOR MENUE :")
  print("1) Addition +: ")
  print("2) Subtraction-: ")
  print("3) Multiplication X: ")
  print("4) Division/: ")
  print("5) String representation : ")
  print("6) Boolean representation : ")
  print("7) Exit: ")
  
  choise=int(input("Enter your choice from 1 to 7: "))
  if choise==7:
    print("Exiting the program") 
    break  
  calc=calculator(a,b)
  a=int(input("Enter first number: "))
  b=int(input("Enter second number: "))
  if choise==1:
    print("Addition:",calc.add())   
  elif choise==2:
    print("Subtraction:",calc.sub())
  elif choise==3:
    print("Multiplication:",calc.mul())       
  elif choise==4:
    a=float(calc.div())
    print("Division:",a)
  elif choise==5:
    print(calc.str())
  elif choise==6: 
    print("Boolean representation:",calc.bool())
  else:
    print("Invalid input")

