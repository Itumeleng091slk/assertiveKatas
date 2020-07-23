morse_dict = { 'A':'.-', 'B':'-...', 
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
				'(':'-.--.', ')':'-.--.-'}  

def letters_to_morsecode(message):
    decoding_message = ' '
    for char in message:
        if char != ' ':
            decoding_message += morse_dict[char] + ' '
        else:
            decoding_message += ' '  
    return decoding_message

def count_characters_in_morsecode(message):
    count = 0
    for char in message: 
        if (char.isspace()) == False: 
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
                decoded_message += list(morse_dict.keys())[list(morse_dict.values()).index(encoded_message)] 
                encoded_message = ''            
    return decoded_message 

def main():
    message = input('enter your message/letter: ').upper()
    decoding = letters_to_morsecode(message)
    count_space = count_characters_in_morsecode(message)

    assert count_space != False, "right number of spaces represented in the output"
    assert len(message) != morsecode_to_letters, "output and input both have the same number of characters represented"
    
    print(f'morse coded message:{decoding}\nOriginal message/Letter: {message}')
    print(len(message))
    
 
    
if __name__ == "__main__":
    main()
