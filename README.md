# 🛡️ Caesar Cipher CLI Tool 🛡️

Welcome to the **Caesar Cipher CLI Tool**, your gateway to ancient cryptography in the digital age! Encrypt and decrypt your secret messages just like Julius Caesar did—but with a modern twist! 🚀

---

## 🎯 Features
- 🔒 **Encrypt Messages**: Secure your text by shifting letters forward in the alphabet.  
- 🔓 **Decrypt Messages**: Reveal the hidden text by reversing the shift.  
- 🧩 **Handles Non-Alphabet Characters**: Retains spaces, numbers, and special characters as-is.  
- 🔄 **Interactive Mode**: Encrypt or decrypt messages in an endless loop (until you say "no").  
- 🌟 **Customizable Shift Amounts**: Specify how much you want to shift the letters.  

---

## 🚀 How It Works
The Caesar Cipher shifts each letter in your message by a specified amount across the alphabet. Non-alphabet characters (like spaces, punctuation, and numbers) remain unchanged.

For example:
- **Input**: `"hello world!"`  
- **Shift**: `3`  
- **Encoded Output**: `"khoor zruog!"`  

---

## 🛠️ Setup and Usage

### 1️⃣ Prerequisites
- Python 3.x installed on your system.

### 2️⃣ Installation
1. Clone this repository:  
   ```bash
   git clone https://github.com/Deepikat11/caesar_cipher.git
   cd caesar-cipher-cli
2.Install the art module:
  ```bash
  python caesar_cipher.py
```
3. Run the Program
  ```bash
  python caesar_cipher.py
```

---

###📖 How to Use
Choose Action:
Enter encode to encrypt or decode to decrypt a message.

Input Message:
Type your secret message (letters, numbers, and symbols are all accepted).

Enter Shift Number:
Choose how many steps you want to shift letters (positive integers only).

Repeat or Exit:
Type yes to process another message or no to exit.

---

###✨ Example Interaction

Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world!
Type the shift number:
3
Here is the encoded result: khoor zruog!

Type 'yes' if you want to go again. Otherwise, type 'no':
yes
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
khoor zruog!
Type the shift number:
3
Here is the decoded result: hello world!

Type 'yes' if you want to go again. Otherwise, type 'no':
no
Goodbye!

---

###🧠 How It’s Built
This project leverages the following:

Python Fundamentals: Loops, conditionals, and string manipulation.
art Module: For a cool ASCII logo display.
Modular Design: Interactive user input and logic encapsulated in a clean function.

---

###📜 License
This project is open source under the MIT License—feel free to use, modify, and share it as you like.

---

###🙌 Acknowledgments
Special thanks to the idea of cryptography and Julius Caesar, who unknowingly inspired one of the oldest encryption methods still studied today!


