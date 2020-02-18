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
    #assert words != 0 , ("Does not have the right number of spaces represented in the output")
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
    assert words != 0 , ("doesn't have the right number of spaces represented in the output") # if you make word <= 0 the assertion error will occur
    return decipher


def main():
    message1 = ("Hi-There")
    result = letters_To_Morsecode(message1.upper())
    #assert len(message1) != 0 , "Does not have the same number of characters in the input & output"
    print(result)
    print(len(message1))


    message2 = ".... .. -....- - .... . .-. ." # if you add another morsecode to this message the assertion will not run because it is true.
    result = morseCode_To_Letters(message2)
    msg_length = list(message2.split(' '))
    assert len(message1) != message2 , "Does not have the same number of characters in the input & output" "Does not have the same number of characters in the input & output" # if you make message1 == message2 and if either one was updated with one character the assertion error will occur.
    print(result)
    print(len(msg_length))

if __name__ == '__main__':
    main()
