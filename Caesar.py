alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(msg, key, mode):
        text = ""
        new_position = 0
        if mode == "decode":
            key *= -1
        for letter in msg:
            if letter not in alphabet:
                text += letter
            else:
                position = alphabet.index(letter)
                new_position = position + key
                if new_position > 25 or new_position < 0:
                    new_position %= 26      
                new_letter = alphabet[new_position]
                text += new_letter         
        print(f"\nThe {mode}d text is : {text}")
            
repeat = 'y'

while repeat == 'y':
    direction = input("\nType 'Encode' to encrypt, type 'Decode' to decrypt : ").lower()
    if direction not in ['encode', 'decode']:
        print("Invalid input!")   
        exit()
    text = input("\nType your message : ").lower()
    shift = int(input("\nType the shift number : "))
    caesar(text, shift, direction)
    flag = 1
    while flag == 1:
        repeat = input("\nY/N to continue : ").lower()
        if repeat == 'y' or repeat =='n':
            flag = 0
        else:
            print("\nInvalid input!!")
        
     

