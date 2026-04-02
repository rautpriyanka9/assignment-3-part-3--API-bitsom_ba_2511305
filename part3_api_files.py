# Task 1 — File Read & Write

# Part A: Write 

file = open("python_notes.txt", "w", encoding="utf-8")

file.write("Topic 1: Variables store data. Python is dynamically typed.\n")
file.write("Topic 2: Lists are ordered and mutable.\n")
file.write("Topic 3: Dictionaries store key-value pairs.\n")
file.write("Topic 4: Loops automate repetitive tasks.\n")
file.write("Topic 5: Exception handling prevents crashes.\n")

file.close()

print("File written successfully.")
file = open("python_notes.txt", "a", encoding="utf-8")

file.write("Topic 6: Functions help reuse code.\n")
file.write("Topic 7: Python supports object-oriented programming.\n")

file.close()

print("Lines appended successfully.")
# -------- Part B: Read --------

file = open("python_notes.txt", "r", encoding="utf-8")

lines = file.readlines()

file.close()
print("\nFile Contents:\n")

count = 0

for line in lines:
    count += 1
    print(f"{count}. {line.strip()}")
print("\nTotal number of lines:", count)

keyword = input("\nEnter keyword to search: ").lower()

found = False

for line in lines:
    if keyword in line.lower():
        print(line.strip())
        found = True

if not found:
    print("No matching lines found.")
    