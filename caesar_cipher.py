def caesar_cipher_encode(message, shift):
    encoded_message = []
    
    for char in message:
        if char.isalpha(): 
            base = ord('A') if char.isupper() else ord('a')
           
            encoded_char = chr((ord(char) - base + shift) % 26 + base)
            encoded_message.append(encoded_char)
        else:
            encoded_message.append(char) 
    
    return ''.join(encoded_message)

def caesar_cipher_decode(encoded_message, shift):
    return caesar_cipher_encode(encoded_message, -shift)

# Example :
message = "Hello, World!"
shift = 3

encoded_message = caesar_cipher_encode(message, shift)
print("Encoded:", encoded_message)

decoded_message = caesar_cipher_decode(encoded_message, shift)
print("Decoded:", decoded_message)