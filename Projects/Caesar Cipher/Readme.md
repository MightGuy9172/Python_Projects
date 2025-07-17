# Caesar Cipher

A simple Python implementation of the classic Caesar Cipher encryption and decryption algorithm. This program allows you to encode or decode messages by shifting the letters of the alphabet by a specified number.

## Features

- Encrypt (encode) messages using a shift value.
- Decrypt (decode) messages using the same shift value.
- Handles both encoding and decoding in a user-friendly loop.
- Preserves non-alphabetic characters (spaces, punctuation, etc.).
- ASCII art logo for a fun interface.

## How It Works

The Caesar Cipher shifts each letter in the message by a fixed number (the shift value). For example, with a shift of 3, `a` becomes `d`, `b` becomes `e`, and so on. Decoding reverses the process.

## Usage

1. **Run the script**:

```sh
python caesar_cipher.py
```

2. **Follow the prompts**:

- Choose to `encode` or `decode`.
- Enter your message.
- Enter the shift number (any integer; it will be normalized to the range 0–25).
- View the result.
- Choose to restart or end the program.

## Example

Type 'encode' to encrypt, type 'decode' to decrypt: encode Type your message: hello world Type the shift number: 3

encoded text is: khoor zruog

## Notes

- The cipher only shifts lowercase alphabetic characters (`a-z`). Other characters remain unchanged.
- The shift value wraps around the alphabet (e.g., shifting `z` by 1 becomes `a`).
- The program continues to run until you choose to end it.

## License

This project is open-source and free to use for educational purposes.

## Author

Created by Manish Maurya.
