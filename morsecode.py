MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ', ':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-'
}

MORSE_CODE_DICT_REV = {v: k for k, v in MORSE_CODE_DICT.items()}
def letters_To_Morsecode(message):
    cipher =''
    for letter in message:
        if letter  != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher +=''
    return cipher

def morseCode_To_Letters(message):
    message += ' '
    decipher = ''
    citext = ''
    space = 0
    for letter in message:
        if (letter != ' '):
            space = 0 
            citext += letter
        else:
            space += 1
            if space == 2 :
                decipher += ' '
            elif citext != '':
                decipher += MORSE_CODE_DICT_REV[citext]
                citext = ''
    return decipher


def main():
    message = ("Hi There")
    result = letters_To_Morsecode(message.upper())
    print(result)

    message = ".... .. -....- - .... . .-. ."
    result = morseCode_To_Letters(message)
    print(result)

if __name__ == '__main__':
    main()