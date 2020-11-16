# Cipher wheel with a function for finding an element in a list

# find_in_list function defined here but not called
def find_in_list(query, chars):
# this function is used to find the position of the "query" in the "mainlist". If "query" is in the list then it returns its position, otherwise it returns None
    mainlist_len = len(chars)
    range_for_loop = range(mainlist_len)
    index = None
    for i in range_for_loop:
        element = chars[i]
        if element == query:
            index = i
            break
        return i
# this should return the position of the "query" in the "mainlist"

chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']

# encrypt_message function defined here but not called
def encrypted_message(plain_message):
# this fucnction takes "plain_msg" as an argument and print/return the encrypted message. The "plain_msg" is tranfered into "encrypted_msg" using "shifted_chars" list. Example, if plain_msg = "ng" then n => p, g => i  and hence encrypted_msg = "pi"
    encrypted_message = ""
    for character in plain_message:
      # for character in message
        if character in chars:
            chars_index = find_in_list(character, chars)
            new_chars = shifted_chars(chars_index]
            encrypted_message = encrypted_message + new_chars
        else:
            encrypted_message = encrypted_message + character

# decrypt_message function defined here but not called
def decrypted_message(encrypted_message):
# this fucnction takes "encrypted_msg" as an argument and print/return the encrypted message. The "encrypted_msg" is tranfered into "decrypted_msg" using "shifted_chars" list. Example, if encrypted_msg = "pi" then p => n, i => g  and hence decrypted_msg = "ng"
    decrypted_message = ""
    for character in encrypted_message:
        if character in shifted_chars:
            chars_index = find_in_list(character, shifted_chars)
            new_char = chars[chars_index]
            decrypted_msg = decrypted_message + new_chars
        else:
            decrypted_message = decrypted_message + character


# methods should return or print the new messages.
############################################### Code starts from here ##################################################
flag = True
while flag == True:
    choice = input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively!")
    if choice == 'e':
        plain_message = input("Enter message to encrypt??")
        encrypted_message(plain_message)
    elif choice == 'd':
        encrypted_message= input("Enter message to decrypt?")
        decrypt_message(encrypted_message)
    
    play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
    if play_again == 'Y':
        print("rani")
    elif play_again == 'N':
            break
