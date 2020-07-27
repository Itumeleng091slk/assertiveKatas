MORSE_DICT = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }

MORSE_DICT_REVERSED = {value:key for key,value in MORSE_DICT.items()}

def letters_to_morsecode(message):
    decoding_message = ' ' 
    return ' '.join(MORSE_DICT.get(char.upper()) for char in message)

def count_characters_in_morsecode(message):
    count = 0
    for char in message: 
        if (char.isspace()) == True: 
            count +=1 
    return count

def morsecode_to_letters(morse_code:str):
    morse_code += ' ' 
    return ''.join(MORSE_DICT_REVERSED.get(char) for char in morse_code.split())

def main():

    print(morsecode_to_letters('.... .. -  .... . .-. . '))
    print(letters_to_morsecode('HITHERE'))
    
    morse_code = input('enter your morse code: ').upper()
    message = input('enter your message/letter: ').upper()
    decoding = letters_to_morsecode(message)
    encoding = morsecode_to_letters(morse_code)
    count_space = count_characters_in_morsecode(message)
    
    assert count_space == FALSE, "right number of spaces represented in the output"
    assert len(message) == morsecode_to_letters, "output and input both have the same number of characters represented"
    
    print(f'Original message/Letter:{encoding}\nMorse coded message: {morse_code}')
    print(f'The length of the message: {len(message)}')
    print(f'The number of spaces in your output:{count_space}')
    print(f'Morse coded message:{decoding}\nOriginal message/Letter: {message}')
    
 
    
if __name__ == "__main__":
    main()
