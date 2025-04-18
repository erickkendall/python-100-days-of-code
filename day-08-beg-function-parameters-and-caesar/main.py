import string
from art import logo


def caesar(original_text, shift_amount, encode_or_decode):

    alphabet = list(string.ascii_lowercase)
    output_text = []

    if encode_or_decode == 'decode':
        shift_amount = shift_amount * -1

    for character in original_text:
        is_uppercase = False  # Reset flag for each character
        alphabet_position = 0
        found = False
    
        if character.isupper():
            is_uppercase = True
            character = character.lower()
    
        for alphabet_position in range(len(alphabet)):
            if character == alphabet[alphabet_position]:
                new_position = (alphabet_position + shift_amount) % len(alphabet)
                encrypted_character = alphabet[new_position]
                if is_uppercase:
                    encrypted_character = encrypted_character.upper()
    
                output_text.append(encrypted_character)
                found = True
                break  # Exit inner loop once found
        
        if not found:
            output_text.append(character)
    
    output_text=''.join(output_text)
    return(output_text)

print(logo)

cipher_active = True

while cipher_active:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n")  # Removed .lower() to preserve uppercase
    shift = int(input("Type the shift number:\n"))
    
    
    result = caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    print(f"The {direction}d message is {result}.")

    while True:
        continue_cipher = input("Any more encoding or decoding? ").lower()
    
        if continue_cipher == "no":
            cipher_active = False
            break
        elif continue_cipher == "yes":
            break
        else:
            print("Please enter yes or no.")
