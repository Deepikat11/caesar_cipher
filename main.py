import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for character in original_text:
        if character in alphabet:
            shifted_position = alphabet.index(character) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        elif character not in alphabet:
            output_text += character
    print(f"Here is the {encode_or_decode}d result: {output_text}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

while True:
    yes_or_no = input("Type 'yes' if you want to go again. Otherwise, type 'no': ").lower()
    if yes_or_no == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    else:
        print("Goodbye!")
        break
