# 1. Display Fibonacci Series up to 10 terms

def fibonacci_series(n):
    fib = [0, 1]
    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])
    return fib
print("Fibonacci Series upto 10 terms:", fibonacci_series(10))


# 2. Display numbers at the odd indices of a list

def odd_indices(lst):
    result = []
    for i in range(len(lst)):
        if i % 2 != 0:
            result.append(lst[i])
    return result
sample_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Numbers at odd indices:", odd_indices(sample_list))


# 3. Count the number of different words in a given text

text = """
I have provided this text to provide tips on creating interesting paragraphs.
First, start with a clear topic sentence that introduces the main idea.
Then, support the topic sentence with specific details, examples, and evidence.
Vary the sentence length and structure to keep the reader engaged.
Finally, end with a strong concluding sentence that summarizes the main points.
Remember, practice makes perfect!
"""

def count_words(text):
    words = text.lower().replace(",", "").replace(".", "").split()
    return len(set(words))
print("Number of different words:", count_words(text))


# 4. Function to count the number of vowels in a word

def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0 
    for char in word:
        if char in vowels:
            count += 1 
    return count 
print("Number of vowels in 'Elephant':", count_vowels("Elephant"))

# 5. Print each animal in all caps

animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']
print("Animals in all caps:")
for a in animals:
    print(a.upper())


# 6. Iterate through numbers 1 to 20 and print if they are odd or even

print("Odd and Even numbers from 1 to 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")


# 7. Function to sum two integers entered by the user

def sum_of_integers(a, b):
    return a + b
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
print("Sum of two integers:", sum_of_integers(a,b))