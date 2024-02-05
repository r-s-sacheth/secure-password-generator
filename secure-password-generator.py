import time
import string
import random
import pyperclip

# Global variable for punctuation characters
global punctuation
punctuation=['!','@','#','$','%','^','&','*','(',')']


def security_notification():
    print('''
    Things to Remember
        > Beware of Phishing Traps
        > Never share your password
        > Enable two-factor authentication 
        > Consider a password manager
        > Regularly update your passwords
    

    Password Security Tips:
        > Use a minimum password length of 10 characters.
        > Include a mix of uppercase and lowercase letters.
        > Add numbers and special characters for complexity.
        > Avoid using easily guessable information (e.g., birthdays, names).
        > Do not reuse passwords across different accounts.
        > Use a unique password for each online service.
        > Regularly update your passwords, especially after security incidents.

    Note:
        > By default, the passwords generated by this program are not stored.
 
    ''')
    time.sleep(1)


def fast_gen(punctuation):
    #Generate a secure random password
    
    punctuation_str=''.join(punctuation)
    characters = string.ascii_letters + string.digits + punctuation_str
    password=''.join(random.choice(characters) for _ in range(random.randint(12,20)))

    #print("\n")
    return password
 

def adv_gen(punctuation):
    #Generate an advanced password with user-specified options  

    print("\n\nSpecify the following parameters for your password:\n")
    total_password_length=int(input("Total Length of the password you need: "))
    punctuation_length=int(input("Total Number of Punctuation Characters you need in your password: "))
    digit_length=int(input("how many digits you want to include: "))
    print("\n")
    
    # Handle the case where the specified total length is less than the sum of punctuation and digit lengths
    if (total_password_length<(punctuation_length+digit_length)):
        
        total_password_length=punctuation_length+digit_length+2
    
    if total_password_length<10:
        print("Not a secure password")
        security=input("Do You want to continue with it? (Y/N): ").strip().lower()=='y'
        if security==False:
            return 0

    if total_password_length>128:
        return 1
    
    rem_character=(total_password_length-(punctuation_length+digit_length))

    punctuation_str=''.join(random.choice(punctuation) for _ in range (punctuation_length))
    digit_str=''.join(random.choice(string.digits) for _ in range(digit_length))
    character_str=''.join(random.choice(string.ascii_letters) for _ in range(rem_character))

    # Combine and shuffle the components to form the final password
    characters = character_str + punctuation_str + digit_str
    password=''.join(random.sample(characters,total_password_length))

    return password


if __name__=="__main__":
    security_notification()
    while True:
        try:
            choice=int(input('''
    Password Generator Options:
        1)Fast Generate  2)Advanced Options  3)Exit
        Choice: '''))
            if choice==1:
                password=fast_gen(punctuation)
                print('''
    Password Generated :)
        Do you want to copy it to the clipboard? ''')
                clipboard=input("(Y/N)  :").strip().lower()=='y'

                if clipboard:
                    pyperclip.copy(password)
                    print('''
    Password copied to the clipboard\n''')
                break

            elif choice==2:
                password=adv_gen(punctuation)

                if password == 0:
                    break
                if password == 1:
                    print("The generated password exceeds 128 characters, which may not be suitable for some systems or services.Exiting...\n")
                    break

                print('''
    Password Generated :)
        Do you want to copy it to the clipboard? ''')
                clipboard=input("(Y/N)  :").strip().lower()=='y'
                if clipboard:
                    pyperclip.copy(password)
                    print('''
    Password copied to the clipboard\n''')
                break

            elif choice==3:
                print("\nExiting... GoodBye :) \n")
                break
            else:
                print("Invalid Choice. Please Try Again!")
                continue
        except ValueError:
            print("Enter a valid Integer Value.\n")
