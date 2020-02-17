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
        if (letter != ' '): # checks for space
            space = 0 # counter to keep track of space
            citext += letter # storing morse code of a single character
        else:  # in case space is not visible/performed 
            space += 1  # indicates a new character
            if space == 2 :  # indicates a new word
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
