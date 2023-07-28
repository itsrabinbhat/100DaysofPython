import string

alphabets = list(string.ascii_lowercase)

# Encryption function
def encode_msg(msg,shift):
    encoded_msg = []
    for letter in msg:
        idx = alphabets.index(letter)
        new_idx = idx + shift
        # print(idx,new_idx)
        if  new_idx >= len(alphabets):
            mod_new_idx = new_idx - len(alphabets)
            encoded_msg.append(alphabets[mod_new_idx])
        else:
            encoded_msg.append(alphabets[new_idx])
    return "".join(encoded_msg)
            

# Decryption function
def decode_msg(txt,shift):
    decoded_msg = []
    for letter in txt:
        idx = alphabets.index(letter)
        new_idx = idx - shift
        decoded_msg.append(alphabets[new_idx])
    
    return "".join(decoded_msg)


c = ''
while c != 'n':
    choice = input("\nEnter 'encode' to encrypt or 'decode' to decrypt:\n").lower()

    if choice == 'encode':
        msg = input("Enter you message:\n").lower()
        shift = int(input("Enter the shift number:\n"))
        e_msg= encode_msg(msg,shift)
        print("Your encrypted text is:",e_msg)
    elif choice == 'decode':
        msg = input("Enter you message:\n").lower()
        shift = int(input("Enter the shift number:\n"))
        d_msg = decode_msg(msg,shift)
        print("Your decrypted text is:",d_msg)
    else:
        print("Invalid choice!")
    
    c = input("Do you want to run the program again(Y/N): ").lower()
