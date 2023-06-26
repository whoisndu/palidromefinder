#!/usr/bin/env python
# coding: utf-8

# In[3]:


def is_palindrome(word):
    # Remove spaces and convert to lowercase
    word = word.replace(" ", "").lower()
    # Check if the word is equal to its reverse
    return word == word[::-1]

def find_palindromes(text):
    # Remove punctuation and convert to lowercase
    text = ''.join(c for c in text if c.isalnum()).lower()
    # Split the text into words
    words = text.split()
    # Initialize a list to store palindromes
    palindromes = []
    # Iterate through each combination of words and check if it is a palindrome
    for i in range(len(words)):
        for j in range(i+1, len(words)+1):
            phrase = ' '.join(words[i:j])
            if is_palindrome(phrase):
                palindromes.append(phrase)
    return palindromes

# Accept text input from the user
text = input("Enter a text: ")
# Find palindromes in the text
found_palindromes = find_palindromes(text)
# Display the palindromes or a message if none found
if found_palindromes:
    print("Palindromes found in the text:")
    for palindrome in found_palindromes:
        print(palindrome)
else:
    print("No palindrome was found in the text.")


# In[ ]:




