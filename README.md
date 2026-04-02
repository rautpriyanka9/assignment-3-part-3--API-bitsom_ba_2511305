# Assignment 3 — Part 3: File I/O, APIs & Exception Handling

##  Overview
This project demonstrates practical usage of:
- File handling (read/write/append)
- API integration using `requests`
- Exception handling for robust programs
- Logging errors to a file with timestamps

The implementation simulates a **Product Explorer system** that interacts with a public API and handles failures gracefully.

---

##  Project Structure

---

##  Requirements

- Python 3.x
- Install required library:
```bash
pip install requests

Tasks implimented
Task1- File read and write 
write noted to python_notes.txt
appends additional lines
reads file and prints numbered content
counts total lines
searches lines based on user input

Task 2 — API Integration

API Used: https://dummyjson.com/products

Features:

Fetch and display 20 products in table format
Filter products with rating ≥ 4.5
Sort filtered products by price (descending)
Fetch laptops category data
Simulate POST request to create a product

Task 3 — Exception Handling
🔹 Part A — Safe Division
Handles:
Division by zero
Invalid data types
🔹 Part B — Safe File Reader
Reads file safely
Handles missing file error
Uses finally block
🔹 Part C — Robust API Calls
Handles:
ConnectionError
Timeout
Generic exceptions
🔹 Part D — Input Validation Loop
Accepts product ID (1–100)
Validates input
Fetches product details from API
Handles 404 errors
Exit using quit

Task 4 — Error Logging

Features:

Logs errors into error_log.txt
Includes timestamp using datetime
Handles:
Connection errors
HTTP errors (e.g., 404)
Displays full log file content at the end

How to Run
python part3_api_files.py