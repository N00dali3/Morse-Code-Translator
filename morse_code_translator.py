from morse import *

def translate_to_morse(letters):
    """Translate words from text to Morse Code."""
    alpha_list = []
    for letter in letters:
        try:
            a2m = alpha_to_morse[letter]
            alpha_list.append(a2m)
        except KeyError:
            return " "
    alpha_morse = " ".join(alpha_list)
    return alpha_morse

def translate_to_alpha(morse):
    """Translate Morse Code to text."""
    morse_list = []
    morse_split = morse.split(" ")
    for x in morse_split:
        try:
            m2a = morse_to_alpha[x]
            morse_list.append(m2a)
        except KeyError:
            return " "
    morse_alpha = "".join(morse_list)
    return morse_alpha

menu = """
Morse Code Translator

0: Exit
1: Translate a word into Morse Code
2: Translate Morse Code to text.
"""
while True:
    
    print(menu)
    selection = input("Please choose option 0, 1, or 2 from the menu above: ")
    
    if selection == '0':
        print("\nDone!")
        break
    
    elif selection == '1':
        word = input("\nPlease enter a word to be translated to Morse Code: ")
        if len(word) > 0:
            word = word.upper()
            alpha2morse = translate_to_morse(word)
            print(f'"{word}" in Morse Code is "{alpha2morse}"')
        else:
            print("Input invalid. Please enter a word. Letters only, no numbers or spaces.")
            continue
          
    elif selection == '2':
        morse_code = input("\nPlease enter Morse Code to be translated to a word: ")
        if len(morse_code) > 0:
            morse2alpha = translate_to_alpha(morse_code)
            print(f'A Morse Code of "{morse_code}" translates to "{morse2alpha}".')
        else:
            print("Invalid input. Please enter Morse Code.")
            continue
        
    else:
        print("\nYour selection is invalid")
        print("Please enter 0, 1, or 2 only.")
        continue
