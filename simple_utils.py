# simple_utils.py - A tiny utility library

def reverse_string(text):
    """
    Reverse the characters in a string.
    
    Parameters:
        text (str): Input string to reverse.
    
    Returns:
        str: The reversed string.
    """
    return text[::-1]

def count_words(sentence):
    """
    Count words in a sentence.
    
    Counts the number of whitespace-separated tokens in the given sentence. Consecutive whitespace is treated as a single separator.
    
    Parameters:
        sentence (str): Input text whose words will be counted.
    
    Returns:
        int: Number of words in the sentence.
    """
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from degrees Celsius to degrees Fahrenheit.
    
    Parameters:
        celsius (float | int): Temperature in degrees Celsius.
    
    Returns:
        float: Temperature converted to degrees Fahrenheit.
    """
    return (celsius * 9/5) + 32