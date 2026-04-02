
# Assignment Part 3


import requests
from datetime import datetime


# LOGGER FUNCTION (Task 4)


def log_error(module, error_type, message):
    with open("error_log.txt", "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] ERROR in {module}: {error_type} — {message}\n")



# TASK 1 — FILE WRITE & READ


print("\n===== Task 1: File Handling =====\n")

# Write
try:
    with open("python_notes.txt", "w", encoding="utf-8") as file:
        file.write("Topic 1: Variables store data. Python is dynamically typed.\n")
        file.write("Topic 2: Lists are ordered and mutable.\n")
        file.write("Topic 3: Dictionaries store key-value pairs.\n")
        file.write("Topic 4: Loops automate repetitive tasks.\n")
        file.write("Topic 5: Exception handling prevents crashes.\n")
    print("File written successfully.")
except Exception as e:
    log_error("file_write", "Exception", str(e))

# Append
try:
    with open("python_notes.txt", "a", encoding="utf-8") as file:
        file.write("Topic 6: Functions help reuse code.\n")
        file.write("Topic 7: Python supports object-oriented programming.\n")
    print("Lines appended successfully.")
except Exception as e:
    log_error("file_append", "Exception", str(e))

# Read
try:
    with open("python_notes.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    print("\n--- File Content ---")
    for i, line in enumerate(lines, start=1):
        print(f"{i}. {line.strip()}")

    print("\nTotal number of lines:", len(lines))

    keyword = input("\nEnter keyword to search: ").lower()
    found = False

    for line in lines:
        if keyword in line.lower():
            print(line.strip())
            found = True

    if not found:
        print("No matching lines found.")

except Exception as e:
    log_error("file_read", "Exception", str(e))



# TASK 2 — API INTEGRATION


print("\n===== Task 2: API Integration =====\n")

# Fetch products
try:
    url = "https://dummyjson.com/products?limit=20"
    response = requests.get(url, timeout=5)
    data = response.json()

    print("ID | Title | Category | Price | Rating")
    print("-" * 60)

    for p in data["products"]:
        print(f"{p['id']} | {p['title']} | {p['category']} | ${p['price']} | {p['rating']}")

except requests.exceptions.ConnectionError as e:
    print("Connection failed.")
    log_error("fetch_products", "ConnectionError", str(e))

except requests.exceptions.Timeout:
    print("Request timed out.")
    log_error("fetch_products", "Timeout", "Request timed out")

except Exception as e:
    log_error("fetch_products", "Exception", str(e))


# Filter & sort
try:
    filtered = [p for p in data["products"] if p["rating"] >= 4.5]
    filtered.sort(key=lambda x: x["price"], reverse=True)

    print("\n--- Filtered Products (Rating >= 4.5) ---")
    for p in filtered:
        print(f"{p['title']} - ${p['price']} - Rating: {p['rating']}")

except Exception as e:
    log_error("filter_sort", "Exception", str(e))


# Laptops category
try:
    url2 = "https://dummyjson.com/products/category/laptops"
    response2 = requests.get(url2, timeout=5)
    data2 = response2.json()

    print("\n--- Laptops ---")
    for item in data2["products"]:
        print(f"{item['title']} - ${item['price']}")

except Exception as e:
    log_error("laptops_fetch", "Exception", str(e))


# POST request
try:
    print("\nCreating New Product...\n")

    post_url = "https://dummyjson.com/products/add"

    new_product = {
        "title": "My Custom Product",
        "price": 999,
        "category": "electronics",
        "description": "A product I created via API"
    }

    response3 = requests.post(post_url, json=new_product, timeout=5)

    print("Response from server:")
    print(response3.json())

except Exception as e:
    log_error("post_product", "Exception", str(e))



# TASK 3 — EXCEPTION HANDLING


print("\n===== Task 3: Exception Handling =====\n")

# Part A: Safe Divide
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))


# Part B: Safe File Reader
def read_file_safe(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File operation attempt complete.")

print("\nReading python_notes.txt:")
print(read_file_safe("python_notes.txt"))

print("\nReading ghost file:")
print(read_file_safe("ghost_file.txt"))


# Part D: Input Validation Loop
print("\n===== Product Lookup =====")

while True:
    user_input = input("Enter product ID (1–100) or 'quit': ")

    if user_input.lower() == "quit":
        print("Exiting program.")
        break

    if not user_input.isdigit():
        print("Invalid input! Enter a number.")
        continue

    product_id = int(user_input)

    if product_id < 1 or product_id > 100:
        print("Please enter ID between 1 and 100.")
        continue

    try:
        url = f"https://dummyjson.com/products/{product_id}"
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            product = response.json()
            print(f"{product['title']} - ${product['price']}")
        elif response.status_code == 404:
            print("Product not found.")
            log_error("lookup_product", "HTTPError", f"404 Not Found for product ID {product_id}")

    except requests.exceptions.ConnectionError:
        print("Connection failed.")
        log_error("lookup_product", "ConnectionError", "No internet")

    except requests.exceptions.Timeout:
        print("Request timed out.")
        log_error("lookup_product", "Timeout", "Request timeout")

    except Exception as e:
        log_error("lookup_product", "Exception", str(e))



# TASK 4 — LOGGING


print("\n===== Task 4: Logging =====\n")

# Trigger Connection Error
try:
    bad_url = "https://this-host-does-not-exist-xyz.com/api"
    requests.get(bad_url, timeout=5)
except requests.exceptions.ConnectionError as e:
    print("Connection failed (intentional).")
    log_error("fetch_products", "ConnectionError", str(e))

# Trigger HTTP error
try:
    response = requests.get("https://dummyjson.com/products/999", timeout=5)
    if response.status_code != 200:
        print("Product not found (intentional).")
        log_error("lookup_product", "HTTPError", "404 Not Found for product ID 999")
except Exception as e:
    log_error("lookup_product", "Exception", str(e))


# Print log file
print("\n----- Error Log Contents -----\n")
try:
    with open("error_log.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("No logs found.")