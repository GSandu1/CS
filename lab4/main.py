import random
import string

PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

# Function to perform the PC1 permutation
def apply_PC1(key_64_bit):
    key_56_bit = "".join([key_64_bit[i-1] for i in PC1])
    return key_56_bit

def generate_random_key():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

def get_key():
    while True:
        print("1 - Input key manually")
        print("2 - Generate key randomly")
        choice = input("Choose an option: ")

        if choice == "1":
            user_key = input("Enter an 8-character key: ")
            if len(user_key) == 8:
                return user_key
            else:
                print("Invalid key length. Key must be 8 characters.")
        elif choice == "2":
            random_key = generate_random_key()
            print(f"Randomly generated key: {random_key}")
            return random_key
        else:
            print("Invalid option. Please enter 1 or 2.")

def main():
    key = get_key()

    # Convert the key to a binary representation
    key_64_bit = ''.join(format(ord(i), '08b') for i in key)

    # Apply the PC1 permutation to get the K+ (56-bit key)
    key_56_bit = apply_PC1(key_64_bit)

    print(f"K+ (56-bit key): {key_56_bit}")

if __name__ == "__main__":
    main()
