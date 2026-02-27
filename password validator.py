'''
len()
count()
'''

def main():
    #rules for creating a strong password
    password_rules = 'The password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit.'
    print(password_rules)
    #asking user to create a password
    #password = input('Enter your password: ')
    #simply check if all the rules for creating a strong password are followed
    

def case_validator(password): # (case rule) this function checks whether the password created has both  uppercase and lower case letters
    if not any(char.isupper() for char in password):
        print('password must have an uppercase and lowercase letter check your password and try again')
    elif not any (char.islower() for char in password):
        print('password must have lowercase letter check your password and try again')    
    else:
        print('password has at least one uppercase and lowercase letter✅')
def length_validator(password):# (length rule) this function checks if the password's lengthe is 8 to 20 characters long
    #checking if the password is in range
    if len(password) <8 or len(password)>16: 
        print('Password must be between 8 and 16 characters long check your password and try again')
    elif len(password)>= 8 and len(password)<=16:
        print('password in range✅')
    
def digit_validator(password):#(numerical rule) this function checks whether the password contains numerical characters
    if not any(char.isdigit() for char in password):
        print('Password must contain at least one digit check your password and try again')
    else:
        print('password contains at least one numerical character✅')
        

    
while True:# this loop will keep running until the user creates a strong password that follows all the rules and breaks the loop
    password = input('Enter your password: ')
    case_validator(password)
    length_validator(password)
    digit_validator(password)
    if (any(char.isupper() for char in password) and any (char.islower() for char in password) and len(password)>= 8 and len(password)<=16 and any(char.isdigit() for char in password)):
        print('password is strong✅')
        break
    
            
        
            

    

main()
