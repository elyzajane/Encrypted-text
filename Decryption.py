#Elyza Jane G. Relucio
Activity = "\033[95mAssignment No. 2"
print(Activity)

#pseudocode
#ask the user to input encrypted text, then decrypt it
input_encrypted_str = input("Enter a string to decrypt: ")
output_decrypted_str = ""
#check every character
for i in range (len(input_encrypted_str)):
#if the character is *, change it to a
    if input_encrypted_str[i] == "*":
        output_decrypted_str += "a"
#if the character is &, change it to e
    elif input_encrypted_str[i] == "&":
        output_decrypted_str += "e"
#if the character is #, change it to i
    elif input_encrypted_str[i] == "#":
        output_decrypted_str += "i"
#if the character is +, change it to o
    elif input_encrypted_str[i] == "+":
        output_decrypted_str += "o"
#if the character is !, change it to u
    elif input_encrypted_str [i] == "!":
        output_decrypted_str += "u"

    else:
        output_decrypted_str += input_encrypted_str[i]    
#print the output
print("The Plain Text:", output_decrypted_str)