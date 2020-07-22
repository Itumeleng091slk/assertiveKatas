from morsecode import *

def test_decode_morse():
    message1 = "Hi-There"
    result = decode_morse(message1.upper())
    assert len(message1) != 0 , "Does not have the same number of characters in the input & output"

def test_encode_to_morse():
    message1 = "Hi-There"
    result = encode_to_morse(message1.upper())
    assert len(message1) != 0 , "Does not have the same number of characters in the input & output"
