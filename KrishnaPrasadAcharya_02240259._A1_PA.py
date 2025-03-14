import requests

# Function 1: Prime Number Sum Calculator
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_sum(start, end):
    total = 0
    for num in range(start, end + 1):
        if is_prime(num):
            total += num
    return total

# Function 2: Length Unit Converter
def length_converter(value, direction):
    if direction == 'M':
        return round(value * 3.28084, 2)  # Meters to Feet
    elif direction == 'F':
        return round(value / 3.28084, 2)  # Feet to Meters
    else:
        return "Invalid direction"

# Function 3: Consonant Counter
def consonant_counter(text):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in text if char in consonants)

# Function 4: Min-Max Number Finder
def min_max_finder(numbers):
    return f"Smallest: {min(numbers)}, Largest: {max(numbers)}"

# Function 5: Palindrome Checker
def is_palindrome(text):
    text = ''.join(text.split()).lower()  # Remove spaces and convert to lowercase
    return text == text[::-1]

# Function 6: Word Counter (from file)
def word_counter_from_file():
    url = 'https://gist.github.com/konrados/a1289ade329ac6f4598ebf5ee3dbcb3c'
    response = requests.get(url)
    text = response.text.lower()
    words_to_count = ['the', 'was', 'and']
    
    word_counts = {word: text.split().count(word) for word in words_to_count}
    return word_counts

# Main Menu Loop
def main():
    while True:
        print("\nMenu:")
        print("1. Prime Number Sum Calculator")
        print("2. Length Unit Converter")
        print("3. Consonant Counter")
        print("4. Min-Max Number Finder")
        print("5. Palindrome Checker")
        print("6. Word Counter (from file)")
        print("7. Exit")

        choice = input("Enter the number of the function you want to use: ")

        if choice == '1':
            start = int(input("Enter the start range: "))
            end = int(input("Enter the end range: "))
            print(f"Sum of primes in range {start} to {end} is: {prime_sum(start, end)}")
        
        elif choice == '2':
            value = float(input("Enter a value: "))
            direction = input("Enter conversion direction ('M' for meters to feet, 'F' for feet to meters): ").upper()
            print(f"Converted length: {length_converter(value, direction)}")
        
        elif choice == '3':
            text = input("Enter a text string: ")
            print(f"Number of consonants: {consonant_counter(text)}")
        
        elif choice == '4':
            num_count = int(input("How many numbers do you want to enter? "))
            numbers = [int(input(f"Enter number {i + 1}: ")) for i in range(num_count)]
            print(min_max_finder(numbers))
        
        elif choice == '5':
            text = input("Enter a text string: ")
            print(f"Is the string a palindrome? {is_palindrome(text)}")
        
        elif choice == '6':
            word_counts = word_counter_from_file()
            for word, count in word_counts.items():
                print(f"'{word}' appears {count} times.")
        
        elif choice == '7':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice, please select a number between 1 and 7.")

if __name__ == '__main__':
    main()
