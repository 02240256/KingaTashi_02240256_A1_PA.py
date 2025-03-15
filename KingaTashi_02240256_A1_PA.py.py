
import re
import math
# Check if the number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i ==0:
            return False
    return True
# calculate the sum of prime numbers within a range.
def prime_sum(start, end):
    return sum(n for n in range(start, end+1) if is_prime(n))

# convert meters to feet or feet to meters
def length_converter(value, direction):
    if direction.upper() == 'M':
        return round(value * 3.28084, 2)
    elif direction.upper() == 'F':
        return round(value/3.28084, 2)
    else:
        raise ValueError("Invalid conversion direction. Use 'M' or 'F'.")

# count the number of consonants in a string.
def consonant_counter(text):
        return sum(1 for char in text if char.isalpha() and char.lower()not in 'aeiou')

# find the minimum and maximum numbers in a list.
def min_max_finder(numbers):        
        return min(numbers,), max(numbers)

# check if the string is a palindrome(ignoring spaces and case).
def is_palindrome(text):
    clean_text = re.sub(r'\s+', '', text).lower()
    return clean_text == clean_text[::-1]

# Counts occurrences of specific words in a file without using regex.
def word_counter(file_path):    
    target_words = {"the": 0, "was": 0, "and": 0}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.split()
                for word in words:
                    cleaned_word = "".join(char.lower() for char in word if char.isalnum())  
                    if cleaned_word in target_words:
                        target_words[cleaned_word] += 1
                    
    except FileNotFoundError :
        return "File not found."
    return target_words
    

while True:
    print("\nMenu:")
    print("1. Prime Number Sum Calculator")
    print("2. Length Unit Converter")
    print("3. Consonant Counter")
    print("4. Min-Max Number Finder")
    print("5. Palindrome Checker")
    print("6. Word Counter ")
    print("7. Exit")
    
    choice = input("Select an option(1-7): ")
    
    if choice == "1":
        try:
            start = int(input("Enter start of range: "))
            end = int(input("Enter end of range "))
            print("Sum of primes:", prime_sum(start, end))
        except ValueError:
            print("invalid input. please enter integers.")
            
    elif choice == '2':
        try:
            value = float(input("Enter the length value: "))
            direction = input("Enter 'M' for meters to feet or 'F' for feet to meters: ")
            print("converted length:", length_converter(value, direction))
        except ValueError:
            print("Error:", e)
            
    elif choice == '3':
        text = input("Enter text: ")
        print("Number of consonants:", consonant_counter(text))
        
    elif choice == '4':
        try:
            count = int(input("How many nubers will you enter?" ))
            numbers = [float(input(f"Enter number : ")) for i in range(count)]
            smallest, largest = min_max_finder(numbers)
            print(f"Smallest: {smallest}, Largest: {largest}")
        except ValueError:
            print("Invalid input. please enter numbers only.")
            
    elif choice == '5':
        text = input("Enter text: ")
        print("palindrome:", is_palindrome(text))
        
    elif choice == '6':
        file_path = input("Enter the path to the text file.")
        print("Word count:", word_counter(file_path))
    
    elif choice == '7':
        print("Exitng program. ")
        break
    else:
        print("Invalid selection! Please choose a valid option")
        
