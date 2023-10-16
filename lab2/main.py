ROMAN_ALPHABET = 'AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ'

def validate_input(text):
    if not all(c.upper() in ROMAN_ALPHABET for c in text):
        raise ValueError("Textul poate conține doar litere din alfabetul român.")

def encode_char(c):
    if c.upper() in ROMAN_ALPHABET:
        return ROMAN_ALPHABET.index(c.upper())
    else:
        raise ValueError(f"Caracterul {c} nu este valid.")

def decode_char(c):
    return ROMAN_ALPHABET[c]

def vigenere_encrypt(plain_text, key):
    validate_input(plain_text)
    validate_input(key)

    if len(key) < 7:
        raise ValueError("Lungimea cheii trebuie să fie cel puțin 7.")

    plain_text = plain_text.replace(" ", "").upper()
    key = key.upper()

    encrypted_text = ""

    for i, c in enumerate(plain_text):
        ki = encode_char(key[i % len(key)])
        ci = (encode_char(c) + ki) % len(ROMAN_ALPHABET)
        encrypted_text += decode_char(ci)

    shifted_alphabet = shift_alphabet_based_on_key(key)
    print("Alfabetul deplasat: ", shifted_alphabet)
    return encrypted_text

def shift_alphabet_based_on_key(key):
    shifted_alphabet = ""
    key = key.upper()
    for i, c in enumerate(ROMAN_ALPHABET):
        ki = encode_char(key[i % len(key)])
        shifted_char = decode_char((encode_char(c) + ki) % len(ROMAN_ALPHABET))
        shifted_alphabet += shifted_char
    return shifted_alphabet

def vigenere_decrypt(cipher_text, key):
    validate_input(cipher_text)
    validate_input(key)

    if len(key) < 7:
        raise ValueError("Lungimea cheii trebuie să fie cel puțin 7.")

    cipher_text = cipher_text.replace(" ", "").upper()
    key = key.upper()

    decrypted_text = ""

    for i, c in enumerate(cipher_text):
        ki = encode_char(key[i % len(key)])
        ci = (encode_char(c) - ki) % len(ROMAN_ALPHABET)
        decrypted_text += decode_char(ci)

    return decrypted_text

while True:
    try:
        operation = input("Alege operația (criptare/decriptare) sau 0 pentru a opri:\n"
                          "1 - criptare\n"
                          "2 - decriptare\n"
                          "0 - oprire\n").lower()

        if operation == '0':
            print("Oprire program.")
            break

        key = input("Introdu cheia: ")
        text = input("Introdu textul: ")

        if operation == '1':
            print("Text criptat:", vigenere_encrypt(text, key))
        elif operation == '2':
            print("Text decriptat:", vigenere_decrypt(text, key))
        else:
            print("Operație invalidă.")
    except ValueError as e:
        print(e)
