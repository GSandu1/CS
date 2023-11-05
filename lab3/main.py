ROMANIAN_CHARS = 'AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZAĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ'

def check_valid_text(input_text):
    if not all(char.upper() in ROMANIAN_CHARS for char in input_text):
        raise ValueError("The text can contain letters just from Romanian alphabet.")

def get_char_index(char):
    if char.upper() in ROMANIAN_CHARS:
        return ROMANIAN_CHARS.index(char.upper())
    raise ValueError(f"{char} character is not valid.")

def get_char_from_index(index):
    return ROMANIAN_CHARS[index]

def cipher_text(message, cipher_key):
    check_valid_text(message)
    check_valid_text(cipher_key)

    if len(cipher_key) < 7:
        raise ValueError("The key length should be not less than 7.")

    message = message.replace(" ", "").upper()
    cipher_key = cipher_key.upper()

    ciphered_text = ""

    for index, char in enumerate(message):
        key_index = get_char_index(cipher_key[index % len(cipher_key)])
        cipher_index = (get_char_index(char) + key_index) % len(ROMANIAN_CHARS)
        ciphered_text += get_char_from_index(cipher_index)

    shifted_chars = get_shifted_chars(cipher_key)
    print("Shifted characters: ", shifted_chars)
    return ciphered_text

def get_shifted_chars(cipher_key):
    shifted_chars = ""
    cipher_key = cipher_key.upper()

    for index, char in enumerate(ROMANIAN_CHARS):
        key_index = get_char_index(cipher_key[index % len(cipher_key)])
        shifted_char_index = (get_char_index(char) + key_index) % len(ROMANIAN_CHARS)
        shifted_chars += get_char_from_index(shifted_char_index)

    return shifted_chars

def decipher_text(encrypted_text, cipher_key):
    check_valid_text(encrypted_text)
    check_valid_text(cipher_key)

    if len(cipher_key) < 7:
        raise ValueError("The key length should be not less than 7.")

    encrypted_text = encrypted_text.replace(" ", "").upper()
    cipher_key = cipher_key.upper()

    deciphered_text = ""

    for index, char in enumerate(encrypted_text):
        key_index = get_char_index(cipher_key[index % len(cipher_key)])
        decipher_index = (get_char_index(char) - key_index) % len(ROMANIAN_CHARS)
        deciphered_text += get_char_from_index(decipher_index)

    return deciphered_text

while True:
    try:
        choice = input("Choose operation (1 - encrypt, 2 - decrypt, 0 - stop):\n").lower()

        if choice == '0':
            print("Exiting program.")
            break

        cipher_key = input("Enter the key: ")
        input_text = input("Enter the text: ")

        if choice == '1':
            print("Encrypted text:", cipher_text(input_text, cipher_key))
        elif choice == '2':
            print("Decrypted text:", decipher_text(input_text, cipher_key))
        else:
            print("Invalid choice.")

    except ValueError as error:
        print(error)
