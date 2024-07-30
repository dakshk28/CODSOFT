import random
import array

#defining the main  function
def main():
    
    #taking input for lenght of the password from the user
    len=int(input("Enter the required length of the password: "))

    #providing the digits to choose from
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
    LCASE_CHAR = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
                'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
                'z'] 
    
    UPCASE_CHAR =   ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
                    'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 
                    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                    'Z'] 
    
    SYMB = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
            '*', '(', ')', '<'] 
    
     # creating a combined list of the digits     
    COMBINED = DIGITS + UPCASE_CHAR + LCASE_CHAR + SYMB

     #choosing random digits
    rand_digit = random.choice(DIGITS) 
    rand_upper = random.choice(UPCASE_CHAR) 
    rand_lower = random.choice(LCASE_CHAR) 
    rand_symbol = random.choice(SYMB)

     #creating a temporary 4 digit password
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

     # creating the password for the specified lenght
    for x in range(len - 4): 
        temp_pass = temp_pass + random.choice(COMBINED)
        temp_pass_list = array.array('u', temp_pass) 
        random.shuffle(temp_pass_list)

     #giving the final output 
    password = "" 
    for x in temp_pass_list: 
            password = password + x
    
    print("Here is a stong password according to ur desired length:  ",password) 

print("*********WELCOME TO THE PASSWORD GENERATOR*********\n")
 
# running a loop giving the user a second chance
while True:
     main()
     ch=input("Do you want to create another password(Answer with Y/N): ")
     if ch=="N":
          break
     elif ch=="Y":
          continue
     else:
          print("Invalid Choice")
