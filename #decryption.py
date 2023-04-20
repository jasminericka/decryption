#jasmin ericka celebre
#problem 2 decryption

import pyfiglet
#ask user to input encrypted text
encr_text = input("What is the encrypted text?")
#initialize empty decrypted text
decr_text = " "
#check characters
characters = {
    '*':'a',
    '&':'e',
    '#':'i',
    '+':'o',
    '!':'u'
}
#decrypt
for char in encr_text:
    if char in characters:
        decr_text += characters[char]
    else:
        decr_text += char
#print output
print("=*" * 80)
print(pyfiglet.figlet_format(decr_text, font="smkeyboard", justify="center"))
print("=*" * 80)