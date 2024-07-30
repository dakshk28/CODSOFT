import random
import array
print("*********WELCOME TO THE PASSWORD GENERATOR*********\n")
def main():
len=int(input("Enter the required length of the password: "))

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

COMBINED = DIGITS + UPCASE_CHAR + LCASE_CHAR + SYMB

rand_digit = random.choice(DIGITS) 
rand_upper = random.choice(UPCASE_CHAR) 
rand_lower = random.choice(LCASE_CHAR) 
rand_symbol = random.choice(SYMB)

temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

for x in range(len - 4): 
    temp_pass = temp_pass + random.choice(COMBINED)
    temp_pass_list = array.array('u', temp_pass) 
    random.shuffle(temp_pass_list)

password = "" 
for x in temp_pass_list: 
        password = password + x

print("Here is a stong password according to ur desired length:  ",password) 
