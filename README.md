# Vigenere Cipher Tool

This repository provides a Python program for encrypting and decrypting text using the Vigenere cipher

## Features

- **Encryption/decryption:** Encrypts plaintext or decrypts ciphertext using a Vigenere cipher
- **Key validation:** Ensures that the provided cipher key consists only of alphabetic characters
- **Preserves case:** Maintains the original casing of letters in the input text during encryption and decryption
- **Preserves non-letters:** Any characters that aren't letters are passed through to the output unchanged
- **Interactive interface:** Guides the user through selecting a mode (encrypt/decrypt) and providing the text and key via command-line prompts

## Setup

To set up and run this project locally, follow these steps:

1.  **Clone the repository**

    ```bash
    git clone https://github.com/dbos23/vigenere_cipher
    ```

2.  **cd to the repository's local path**

    ```bash
    cd <path_to_repo>
    ```

3.  **Run the main script**

    ```bash
    python main.py
    ```

## Usage

After running `main.py`, the program will prompt you to select a mode, enter your text, and provide the encryption/decryption key

1.  **Select mode:** Choose either `encrypt` or `decrypt`
2.  **Enter text:** Provide the plaintext for encryption or ciphertext for decryption
3.  **Enter key:** Input the Vigenere cipher key. The key must contain only letters

**Encryption example:**

```bash
python main.py
Select mode (valid options are "encrypt" and "decrypt"): encrypt
Enter plaintext: Hello, world!
Enter encryption key: SECRET
Encrypted text:
Zincs, pgvnu!
```

**Decryption example:**

```bash
python main.py
Select mode (valid options are "encrypt" and "decrypt"): decrypt
Enter encrypted text: Zincs, pgvnu!
Enter decryption key: SECRET
Plaintext:
Hello, world!
```

## Project Structure

```text
.
├── modules/
│   ├── setup.py
│   └── vigenere.py
├── .gitignore
└── main.py
```

## Notes/Design

The project has a main script and a `modules` directory

- **`main.py`**:
  - Orchestrates the process by calling functions from `modules`
  - Handles user interaction, prompting for encryption/decryption mode, text, and key
  - Validates the key using `modules.setup.check_key_validity`
  - Prints the final encrypted or decrypted output from `modules.vigenere.vigenere`

- **`modules/setup.py`**:
  - `check_key_validity(key)`:
    - Ensures that the provided key contains only alphabetic characters, exiting the script if invalid
  - `set_up_vars(text, key)`:
    - Prepares the key for the Vigenere cipher. It extends or truncates the key to match the length of the text and defines two alphabets (lowercase and capital) to allow for case preservation during encryption and decryption

- **`modules/vigenere.py`**:
  - `vigenere(mode, text, key)`:
    - Implements the core Vigenere cipher logic
    - Calls `set_up_vars` to prepare the key and alphabets
    - Iterates through each character of the text, applying the Vigenere shift only to alphabetic characters and leaving the rest as they are
    - Preserves the original case of each letter by mapping to either a lowercase or capital alphabet
