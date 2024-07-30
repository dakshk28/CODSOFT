#defining functions 

#function for addition 
def add(n1,n2):
    return n1+n2
#function for subtraction 
def sub(n1,n2):
    return n1-n2    
#function for multiplication 
def mult(n1,n2):
    return n1*n2
#function for division
def div(n1,n2):
    return n1/n2


#printing  a menu for the user 
print("Select your desired funtion:  \n" \
        "1.Addition\n" \
        "2.Subtraction\n" \
        "3.Multiplication\n" \
        "4.Division\n" )

#taking operation choice from the user
operation=int(input("Enter a choice from the above function (choosing from 1/2/3/4): "))

#taking input from the user
n1=int(input("Enter the first number for the operation: "))
n2=int(input("Enter the second number for the operation: "))


#performing operations based on the chosen option
if operation == 1:
    print(n1, "+", n2,"=",
                add(n1,n2))

elif operation == 2:
    print(n1, "-", n2,"=",
                sub(n1,n2))
    
elif operation == 3:
    print(n1, "X", n2,"=",
                mult(n1,n2))
    
elif operation == 4:
    print(n1, "÷", n2,"=",
                div(n1,n2))
    
else:
    print("Option chosen is not from the list")
