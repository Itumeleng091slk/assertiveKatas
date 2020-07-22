import sys
import string

morse_dict = {
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

inverse_morse_dict = dict((v, k) for (k, v) in morse_dict.items())

test_code = ".... . .-.. .-.. --- / -.. .- .. .-.. -.-- / .--. .-. --- --. .-. .- -- -- . .-. / --. --- --- -.. / .-.. ..- -.-. -.- / --- -. / - .... . / -.-. .... .- .-.. .-.. . -. --. . ... / - --- -.. .- -.--"

def decode_to_morse(message):
    message_separated = message.split(' ')
    decode_message = ''
    for char in message_separated:
        if char in inverse_morse_dict:
            decode_message  += inverse_morse_dict[char]
        else:
            decode_message  += '<CF>' # CF = Character found
    return decode_message 


def encode_to_morse(message):
    encoded_message = ""
    for char in message[:]:
        if char.upper() in morse_dict:
            encoded_message  += morse_dict[char.upper()] + " "
        else:
           encoded_message += '<CF>'
    return encoded_message 

def main():
    message1 = "Hi-There"
    decoding = decode_to_morse(message1.upper())
    print(decoding)
    print(len(message1))


    message2 = ".... .. -....- - .... . .-. ." 
    msg_length = list(message2.split(' '))
    encoding = encode_to_morse(message2)
    print(encoding)
    print(len(msg_length))

if __name__ == '__main__':
    main()
