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

import requests

print("\n===== Task 2: API Integration =====\n")

url = "https://dummyjson.com/products?limit=20"

response = requests.get(url)

data = response.json()

products = data["products"]

print("ID | Title                     | Category     | Price   | Rating")
print("---------------------------------------------------------------")

for p in products:
    print(f"{p['id']:<3}| {p['title'][:25]:<25}| {p['category']:<12}| ${p['price']:<7}| {p['rating']}") 
print("\nHigh Rated Products (rating ≥ 4.5):\n")

filtered = []

for p in products:
    if p["rating"] >= 4.5:
        filtered.append(p)

# sort by price (descending)
filtered.sort(key=lambda x: x["price"], reverse=True)

for p in filtered:
    print(f"{p['title']} - ${p['price']} - Rating: {p['rating']}")
print("\nLaptop Products:\n")

url2 = "https://dummyjson.com/products/category/laptops"

response2 = requests.get(url2)

data2 = response2.json()

laptops = data2["products"]

for item in laptops:
    print(f"{item['title']} - ${item['price']}")
print("\nCreating New Product:\n")

post_url = "https://dummyjson.com/products/add"

new_product = {
    "title": "My Custom Product",
    "price": 999,
    "category": "electronics",
    "description": "A product I created via API"
}

response3 = requests.post(post_url, json=new_product)

print("Response from server:")
print(response3.json())
