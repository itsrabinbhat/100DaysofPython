# lets define a mapping dict
import os

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}


# Encoding functions
def encode_text(msg):
    encoded_text = ''
    for char in msg.upper():
        encoded_text += f'{morse_dict[char]} '
    return encoded_text


# Decoding function
def decode_morse(morse_code):
    decoded_text = ''
    code_list = morse_code.split(' ')
    for code in code_list:
        for char, morse_code in morse_dict.items():
            if code == morse_code:
                decoded_text += char

    return decoded_text


# Clearing the screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# Creating main function to handle user input and result output
def main():
    clear_screen()
    print('--------------WELCOME TO OUT MORSE CODE TRANSLATOR------------------')
    print('Available options:\n'
          '1. Encode text\n2. Decode text\n3. Exit')
    user_choice = input("Enter your choice(1, 2 or 3): ")
    if int(user_choice.strip()) == 1:
        clear_screen()
        to_encode = input("Enter a string to convert it to morse code or enter 'X' to go to main menu: ")
        encoded_text = encode_text(to_encode)
        print(f'\nString: {to_encode}\nMorse code: {encoded_text}')
        if input('\nEnter any key to continue or Enter to exit: '):
            main()
    elif int(user_choice.strip()) == 2:
        clear_screen()
        to_decode = input("Enter morse code to convert it to string or enter 'X' to go to main menu: ")
        decoded_text = decode_morse(to_decode)
        print(f'\nMorse code: {to_decode} \nDecoded String: {decoded_text}')
        if input('\nEnter any key to continue or Enter to exit: '):
            main()
    elif int(user_choice.strip()) == 3:
        exit()
    else:
        print('Invalid choice! Try again...')
        main()


main()
