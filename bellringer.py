import codecs

def rot13(text):
    return codecs.encode(text, 'rot_13')

#Test
message = "Mr. Baez"
encoded_message = rot13(message)
print(encoded_message)
