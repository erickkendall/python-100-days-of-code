# Caesar Cipher

A Python implementation of the classic Caesar cipher encryption and decryption technique.

## Description

This Caesar Cipher program allows users to encrypt and decrypt messages using a simple substitution cipher. The cipher works by shifting each letter in the original message by a specified number of positions in the alphabet. The program preserves case (uppercase/lowercase) and handles non-alphabetic characters (numbers, symbols, spaces) by leaving them unchanged.

The Caesar cipher is one of the earliest and simplest forms of encryption, dating back to Julius Caesar who reportedly used it to communicate with his generals.

## Features

- **Encode/Decode Functionality**: Encrypt or decrypt messages with the same program
- **Case Preservation**: Maintains uppercase and lowercase letters as they appear in the original message
- **Non-Alphabetic Character Support**: Preserves spaces, numbers, and special characters
- **Custom Shift Values**: Use any integer as the shift value (the program handles wrapping around the alphabet)
- **User-Friendly Interface**: Clear prompts and easy-to-understand output
- **ASCII Art Logo**: Visual flair for the program's interface

## How to Use

1. Ensure you have Python installed on your system.
2. Download both files (`main.py` and `art.py`) into the same directory.
3. Run the program from your terminal/command prompt:
   ```
   python main.py
   ```
4. Follow the prompts:
   - Choose to `encode` or `decode` a message
   - Enter the message you want to process
   - Specify the shift number (how many positions to shift each letter)
5. View the result
6. Choose whether to continue with another message or exit

## Example Usage

```
           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           

Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
Hello, World!
Type the shift number:
5
The encoded message is Mjqqt, Btwqi!
Any more encoding or decoding? yes
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
Mjqqt, Btwqi!
Type the shift number:
5
The decoded message is Hello, World!
Any more encoding or decoding? no
```

## How It Works

The Caesar cipher works by shifting each letter in the alphabet by a fixed number of positions:

1. For **encryption** (encode):
   - Each letter is shifted forward in the alphabet by the shift amount
   - For example, with a shift of 3: A → D, B → E, C → F, etc.

2. For **decryption** (decode):
   - Each letter is shifted backward in the alphabet by the shift amount
   - For example, with a shift of 3: D → A, E → B, F → C, etc.

3. **Handling alphabet boundaries**:
   - When shifting reaches the end of the alphabet, it wraps around
   - For example, with a shift of 3: X → A, Y → B, Z → C

4. **Case preservation and non-alphabetic characters**:
   - Uppercase letters remain uppercase after shifting
   - Lowercase letters remain lowercase after shifting
   - Numbers, punctuation, and spaces remain unchanged

## Code Structure

The project consists of two Python files:

1. `main.py` - Contains the main program logic:
   - `caesar()` function that handles the encryption/decryption
   - Main loop for user interaction

2. `art.py` - Contains the ASCII art logo displayed at program start

## Historical Context

The Caesar cipher is named after Julius Caesar, who used it with a shift of 3 to protect messages of military significance. While simple by today's standards, it was effective in its time when many people were illiterate. The cipher demonstrates fundamental principles of substitution that form the basis of more complex encryption methods.

## Security Note

The Caesar cipher is **not** secure for sensitive information in the modern world. With only 26 possible shifts, it can be easily broken by trying all possibilities (brute force attack). This implementation is for educational purposes and entertainment only.

## Credits

This project is part of the "100 Days of Code - Python Pro Bootcamp" curriculum.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
