# Create a variable called shift and assign the value 5 to your new variable.

'''shift = 5'''

# Declare another variable called alphabet and assign the string abcdefghijklmnopqrstuvwxyz to this variable.

'''alphabet = "abcdefghijklmnopqrstuvwxyz"'''

# Create a variable named shifted_alphabet and use the slicing syntax to assign it the portion of alphabet that starts at the index of shift. 
# Then, call the built-in print() function to print shifted_alphabet on the terminal and look at the result.

'''shifted_alphabet = alphabet[shift:]
print(shifted_alphabet)'''

# Modify the existing assignment of the shifted_alphabet variable: use the slicing syntax to extract the missing first portion of alphabet and concatenate it to alphabet[shift:].
# As a reminder, sentence[start:stop] returns the characters of sentence from position start (included) to stop (excluded).

'''shifted_alphabet = (alphabet[shift:] + alphabet[:5])
print(shifted_alphabet)'''

'''shifted_alphabet = (alphabet[shift:] + alphabet[:shift])'''
# print(shifted_alphabet)

# Now that you have your entire shifted alphabet, remove the print(shifted_alphabet) call.

# You'll learn more about the type of structure returned by str.maketrans() later on in the curriculum. 
# For now, create a translation table that maps the characters in alphabet to the characters in shifted_alphabet and assign it to a variable named translation_table.

'''translation_table = str.maketrans(alphabet, shifted_alphabet)'''

# Declare a new variable named text and assign it the string hello world. This will be the message to encrypt.

'''text = "hello world"'''

# Call the translate() method on text passing in the translation_table as the argument and assign the result to a variable named encrypted_text.

'''encrypted_text = text.translate(translation_table)
print(encrypted_text)'''

# Create a function named caesar. 
# Put all your existing code within the function body. 
# Pay attention to keep the same indentation level for all of the lines within the function body.

'''def caesar():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shift = 5
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet, shifted_alphabet)
    text = 'hello world'
    encrypted_text = text.translate(translation_table)
    print(encrypted_text)'''

# The message to encrypt and the shift are still hardcoded in your function. 
# Give your function two parameters named text and shift, and delete the declarations of both the text and shift variables from the caesar function body.

'''def caesar(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet, shifted_alphabet)
    encrypted_text = text.translate(translation_table)
    print(encrypted_text)'''

# Now, test the caesar function by calling it with the string freeCodeCamp and the number 3 as the arguments. 
# Assign the function call to a variable named encrypted_text.

'''encrypted_text = caesar("freeCodeCamp",3)'''

# Now your code is reusable. 
# However, the caesar function prints a message on the terminal and gives back None by default. 
# To prove it, print encrypted_text at the end of your code.

'''print(encrypted_text)'''

# Remove the print(encrypted_text) call from your function. 
# Then, delete the declaration of the encrypted_text variable and return directly text.translate(translation_table) from your function.

def caesar(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(translation_table)  
    
encrypted_text = caesar('freeCodeCamp', 3)
print(encrypted_text)

# Update your str.maketrans() call by concatenating to each argument the uppercase version of the argument itself.

