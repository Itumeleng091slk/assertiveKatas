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
    for char in message: 
        if (char.isspace()) == True: 
            count +=1 
    return count

def morsecode_to_letters(morse_code:str):
    morse_code += ' '
    decode = ''
    encode = ''
    for char in morse_code:
        if char != ' ':
            count = 0
            encode += char
        else:
            count += 1
            if count == 2:
                decode += ' '
            else:
                decode += list(MORSE_DICT.keys())[
                    list(MORSE_DICT.values()).index(encode)
                    ]
                encode = ''
    return decode


def main():
    morse_code = '.... ..  - .... . .-. .'
    decode = morsecode_to_letters(morse_code)
    count_space = count_characters_in_morsecode(morse_code)
    count_space = decode.count(' ')
    print("Encryption:")
    print(f"encoded Message : {decode}")
    print(f"Length of decoded message : {len(decode)}")
    print(f"Number of spaces in the input message: {count_space}")


    message = 'Hi There'.upper()
    encode = letters_to_morsecode(message)
    count_space = message.count(' ')
    print('Decryption:')
    print(f'Input Message Length : {len(message)}')
    print(f'Number of spaces in the encoded message: {count_space}')
    print(f'Encoded Message : {encode}')

 
    assert len(encode) != 0, "You cannot not encrypt an empty message"
    assert len(decode) != 0, "You cannot not decrypt an empty message"
    assert count_space == 1, "encryption and decryption must have same number of spaces in the output"

    
if __name__ == "__main__":
    main()
