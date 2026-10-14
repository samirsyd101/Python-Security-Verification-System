#python program that creates a simple security verification system

#asks user to create pass
password = input("Please create a password:   ")

#creating variable for verification
verification = input("Enter your password again:    ")

#if statement to verify correct password input
if verification == password:
    sensitive_data = input("Nice! Now enter sensitive data information: ")

    #creating variable for encryption 
    encryption = ""

# looping through each character and shifitng it foward by 3. 
    for character in sensitive_data:
        encryption += chr(ord(character) + 3)
#printing the encrypted sensitive data
    print("Encrypted sensitive data: ", encryption)

   #asking user to enter the password again before accessing
    access_pass = input("enter pass to be given access: ")
#checking if the password that is entered is correct
    if access_pass == password:
        print("permission granted")
        print("the encrypted message is: ", encryption)
    #creating an empty string for message that is decrypted
        decrypted = ""

        #reversing the encryption by shifting each character back by 3
        for character in encryption:
            decrypted += chr(ord(character) - 3)
    #displaying the decrypted message
        print("the decrypted message is: ", decrypted)
    else:
        #else statement for incorrect password input
        print("\nverification was failed!")

else:
    #strops the program is the password is not verified or wrong
    print("\nverification was failed")
    print("not given permission")

    