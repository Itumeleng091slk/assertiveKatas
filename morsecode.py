MORSE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "/",
    "1" : ".----",
    "2" : "..---",
    "3" : "...--",
    "4" : "....-",
    "5" : ".....",
    "6" : "-....",
    "7" : "--...",
    "8" : "---..",
    "9" : "----.",
    "0" : "-----",
    ".": ".-.-.-",
    ",": "--..--",
    ":": "---...",
    "?": "..--..",
    "'": ".----.",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "=": "-...-"
} 


def letters_to_morsecode(message):
    decoding_message = ''
    for char in message:
        if char != ' ':
            decoding_message += MORSE_DICT[char] + ' '
        else:
            decoding_message += ' '  
    return decoding_message

def count_characters_in_morsecode(message):
    count = 0
    for char in morsecode_to_letters: 
        if (char.isspace()) == True: 
            count+=1
    return count 

def morsecode_to_letters(message):
    message += ' '
    decoded_message = '' 
    encoded_message = '' 
    for char in message:
        if (char != ' '):
            count = 0
            encoded_message += char 
        else: 
            count += 1 
            if count == 2 : 
                decoded_message += ' '
            else:  
                decoded_message += list(MORSE_DICT.keys())[list(MORSE_DICT .values()).index(encoded_message)] 
                encoded_message = ''            
    return decoded_message  
    
def main():
    
    message = "Hi There"
    expected_output = ".... ..  - .... . .-. ."
    decoding = letters_to_morsecode(message.upper())
    assert len(message) != morsecode_to_letters, "output and input both have the same number of characters represented"
    print(f'decoded message:{decoding}')
    print(len(message))
    
    message = ".... ..  - .... . .-. ."
    msg_len = list(message.split(' '))
    encoding = morsecode_to_letters(message)
    assert len(message) != count_characters_in_morsecode, "right number of spaces represented in the output"
    print(f'encoded Message : {encoding}')
    print(len(msg_len))
    
if __name__ == "__main__":
    main()
