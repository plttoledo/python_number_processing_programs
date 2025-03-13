# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.
# Get 10 user input numbers, print all the numbers. For duplicates, only show one.

numbers = []
entries = []

for i in range(10):
    num = int(input(f"Enter #{i+1}: "))
    numbers.append(num)

for num in numbers:
    if num not in entries:
        print(num)
        entries.append(num)