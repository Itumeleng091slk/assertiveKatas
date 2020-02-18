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

MORSE_CODE_DICT_REV = {v: k for k, v in MORSE_CODE_DICT.items()} #This dictionary maps in reverse, and makes sure a check citext contains at least one character
def letters_To_Morsecode(message):
    cipher =''
    for letter in message:
        if letter  != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher +=''
    #assert letter != message, ("the output and input both have the same number of characters represented")
    assert words != 0 , ("Does not have the right number of spaces represented in the output")
    return cipher

def morseCode_To_Letters(message):
    message += ' '
    decipher = ''
    citext = ''
    words = 0
    for letter in message:
        if (letter != ' '): # checks for space
            words = 0 # counter to keep track of space
            citext += letter # storing morse code of a single character
        else:  # in case space is not visible/performed 
            words += 1  # indicates a new character
            if words == 2 :  # indicates a new word
                decipher += ' '
            elif citext != '': # accessing the keys using their values (reverse of letters_To_Morsecode)
                decipher += MORSE_CODE_DICT_REV[citext]
                citext = ''
    #assert letter != message, ("the right number of spaces represented in the output")
    return decipher


def main():
    message = ("Hi There")
    result = letters_To_Morsecode(message.upper())
    assert len(message) != 0 , "Does not have the same number of characters in the input & output"
    print(result)

    message = ".... .. -....- - .... . .-. ."
    result = morseCode_To_Letters(message)
    print(result)

if __name__ == '__main__':
    main()
