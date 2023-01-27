import calculator


CRED = '\033[91m'
CEND = '\033[0m'


banner = """

    ____        ______      __           __      __            
   / __ \__  __/ ________ _/ _______  __/ ____ _/ /_____  _____
  / /_/ / / / / /   / __ `/ / ___/ / / / / __ `/ __/ __ \/ ___/
 / ____/ /_/ / /___/ /_/ / / /__/ /_/ / / /_/ / /_/ /_/ / /    
/_/    \__, /\____/\__,_/_/\___/\__,_/_/\__,_/\__/\____/_/     
      /____/                                                   



"""

print(banner)

calc = calculator.Calculator()

while True:
	#print("\n")
    print("\nEnter your choice of operation\n1. add\n2. subtract\n3. multiply\n4. divide\n5. exit")
    choice = str(input("Choose one operation : "))
    if (choice == "add" or choice == '1'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(CRED+"\nResult : ", str(calc.add(num1, num2))+CEND)
        
    elif (choice == "subtract" or choice == '2'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(CRED+"\nResult : ", str(calc.subtract(num1,num2))+CEND)

    elif (choice == "multiply" or choice== '3'):
    	num1 = float(input("Enter the first number: "))
    	num2 = float(input("Enter the second number: "))
    	print(CRED+"\nResult : ", str(calc.multiply(num1,num2))+CEND)
    elif (choice == "divide" or choice == '4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(CRED+"\nResult : ", str(calc.divide(num1,num2))+CEND)
    elif (choice == "exit" or choice=='5'):
    	print("Exiting ......")
    	break	
    else:
    	print(CRED+"\nPlease choose one option"+CEND)











