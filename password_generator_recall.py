import random

import array
 

def password_generator():

    # maximum length of password needed
    # this can be changed to suit your password length


    MAX_LEN = 12
     
    # declare arrays of the character that we need in out password
    # Represented as chars to enable easy string concatenation

    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  

    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 

                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',

                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',

                         'z']
     

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 

                         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',

                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',

                         'Z']
     

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 

               '*', '(', ')', '<']
     
    # combines all the character arrays above to form one array

    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
     
    # randomly select at least one character from each character set above

    rand_digit = random.choice(DIGITS)

    rand_upper = random.choice(UPCASE_CHARACTERS)

    rand_lower = random.choice(LOCASE_CHARACTERS)

    rand_symbol = random.choice(SYMBOLS)
     
    # combine the character randomly selected above
    # at this stage, the password contains only 4 characters but 
    # we want a 12-character password

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
     
     
    # now that we are sure we have at least one character from each
    # set of characters, we fill the rest of
    # the password length by selecting randomly from the combined 
    # list of character above.

    for x in range(MAX_LEN - 4):

        temp_pass = temp_pass + random.choice(COMBINED_LIST)
     

        # convert temporary password into array and shuffle to 

        # prevent it from having a consistent pattern

        # where the beginning of the password is predictable

        temp_pass_list = array.array('u', temp_pass)

        random.shuffle(temp_pass_list)
     
    # traverse the temporary password array and append the chars
    # to form the password

    password = ""

    for x in temp_pass_list:

            password = password + x

             
    #returns password to main program

    return password




def file_logger(PW):
    
    file = 'log_master.txt'
    f = open(file, 'a') ##r is to read, w is to write, and a is for append.
    What = input('What is this used for?')
    User = input('username?:')

    f.write('\n')
    f.write("Website/need:" + What + '\n')
    f.write("User:" + User + '\n')  
    f.write("Pass:" + PW +'\n')
    f.close()

    f2 = open(file, 'r')
    last_line = f2.readlines()[-1]
    print(last_line)
    if(last_line == "Pass:" + PW +'\n'):
        print("Logged!")
    else:
        print("Failed")
    f2.close()





def main():
    
    PW = password_generator()
    print(PW + "\nDo you want to generate another password?")
    Bool_1 = input("Y/N:")
    
    if(Bool_1 == "Y" or Bool_1 == "y"):
        main()
    elif (Bool_1 == "N" or Bool_1 == "n"):
        file_logger(PW)
    else:
    	print("invalid input")
    	main()
    
main()
