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

'''def caesar(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(translation_table)  
    
encrypted_text = caesar('freeCodeCamp', 3)
print(encrypted_text)'''

# Update your str.maketrans() call by concatenating to each argument the uppercase version of the argument itself.

'''def caesar(text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), 
        shifted_alphabet + shifted_alphabet.upper()
    )
    return text.translate(translation_table)

encrypted_text = caesar('freeCodeCamp', 3)
print(encrypted_text)'''

# At the beginning of your function body, create an if statement. 
# For now, use True as the condition, and within the if statement body return the string Shift must be an integer value.

'''def caesar(text, shift):

    if True:
        return "Shift must be an integer value."

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), 
        shifted_alphabet + shifted_alphabet.upper()
    )
    return text.translate(translation_table)

encrypted_text = caesar('freeCodeCamp', 3)
print(encrypted_text)'''


# Replace the current condition of your if statement with an isinstance() call. Pass in shift as the first argument, and int as the second argument.

'''def caesar(text, shift):

    if isinstance(shift, int):
        return 'Shift must be an integer value.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), 
        shifted_alphabet + shifted_alphabet.upper()
    )
    return text.translate(translation_table)

encrypted_text = caesar('freeCodeCamp', 3)
print(encrypted_text)'''

# Use the not operator to fix the condition of the if statement so that your function returns Shift must be an integer value. when shift is not an integer.

'''def caesar(text, shift):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), 
        shifted_alphabet + shifted_alphabet.upper()
    )
    return text.translate(translation_table)

encrypted_text = caesar('freeCodeCamp', 3)
print(encrypted_text)'''

# A negative or null shift should not be accepted by your function.
# Therefore, after your first if statement, create another if statement that checks if shift is less than 1 and returns the string Shift must be a positive integer.

'''def caesar(text, shift):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    
    if shift < 1:
        return "Shift must be a positive integer."

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), 
        shifted_alphabet + shifted_alphabet.upper()
    )
    return text.translate(translation_table)

encrypted_text = caesar('freeCodeCamp', 3)
print(encrypted_text)'''

# Add a second condition to the if statement that verifies that shift is greater than 25. 
# Remember that the logical OR operation in Python is implemented through the or operator.
# Also, update the returned message to Shift must be an integer between 1 and 25.

'''def caesar(text, shift):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), 
        shifted_alphabet + shifted_alphabet.upper()
    )
    return text.translate(translation_table)

encrypted_text = caesar('freeCodeCamp', 3)
print(encrypted_text)'''

# Add a third parameter named encrypt to your function and give it a default value of True.

'''def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), 
        shifted_alphabet + shifted_alphabet.upper()
    )
    return text.translate(translation_table)

encrypted_text = caesar('freeCodeCamp', 3)
print(encrypted_text)'''

# Create an if statement that checks if encrypt is not truthy. 
# Within the new if statement, set shift to - shift. 
# This is necessary to enable the shift to take place in the opposite direction with respect to the encryption process.

'''def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if encrypt is False:
        shift = - shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), 
        shifted_alphabet + shifted_alphabet.upper()
    )
    return text.translate(translation_table)

encrypted_text = caesar('freeCodeCamp', 3)
print(encrypted_text)'''

# Declare two functions named encrypt and decrypt, both with text and shift parameters.
# You'll use encrypt for the encryption process, and decrypt for the decryption, labeling the two actions with a descriptive name.
# Return a caesar call passing in text and shift from both your new functions, but make sure to pass in also False as the third argument for the decrypt function.

'''def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if encrypt is False:
        shift = - shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), 
        shifted_alphabet + shifted_alphabet.upper()
    )
    return text.translate(translation_table)

def encrypt(text, shift):
    return caesar(text, shift)
def decrypt(text, shift):
    return caesar(text, shift, False)

encrypted_text = caesar('freeCodeCamp', 3)
print(encrypted_text)'''

# It's time to test the encrypt function. 
# Using the same arguments, replace your caesar call with a call to encrypt. 
# You'll see the same output on the terminal.

'''def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if encrypt is False:
        shift = - shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), 
        shifted_alphabet + shifted_alphabet.upper()
    )
    return text.translate(translation_table)

def encrypt(text, shift):
    return caesar(text, shift)
def decrypt(text, shift):
    return caesar(text, shift, False)

encrypted_text = encrypt('freeCodeCamp', 3)
print(encrypted_text)'''

# Now you're going to test the decrypt function. 
# Replace the value assigned to encrypted_text with the following string, which represents a message to decrypt: Pbhentr vf sbhaq va hayvxryl cynprf..
# Then, declare a variable named decrypted_text and assign it a call to decrypt with encrypted_text as it first argument and a shift of 13 as the second argument.
# Finally, print the decrypted_text on the terminal. With that, the Caesar cipher is complete.

def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'
    
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if encrypt is False:
        shift = - shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), 
        shifted_alphabet + shifted_alphabet.upper()
    )
    return text.translate(translation_table)

def encrypt(text, shift):
    return caesar(text, shift)
def decrypt(text, shift):
    return caesar(text, shift, False)

encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)