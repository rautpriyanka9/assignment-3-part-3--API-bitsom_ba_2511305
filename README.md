# Assignment 3 — Part 3: File I/O, APIs & Exception Handling

## Overview
This project demonstrates practical Python concepts including file handling, API integration, exception handling, and error logging. The program simulates a Product Explorer system that fetches data from a public API and handles failures gracefully.

---

## Project Structure

python-assignment-part3/
│
├── part3_api_files.py
├── python_notes.txt
├── error_log.txt
└── README.md

---

## Requirements

- Python 3.x
- Install required library:

pip install requests

---

## Task 1 — File Read & Write

- Writes 5 predefined lines to python_notes.txt using write mode
- Appends additional lines using append mode
- Reads file and prints numbered lines
- Counts total number of lines
- Allows user to search for a keyword (case-insensitive)

---

## Task 2 — API Integration

API Used: https://dummyjson.com/products

- Fetches 20 products and displays them
- Filters products with rating >= 4.5
- Sorts filtered products by price (descending)
- Fetches laptops category products
- Sends a POST request to simulate product creation

---

## Task 3 — Exception Handling

### Safe Divide
- Handles division by zero
- Handles invalid input types

### Safe File Reader
- Reads file safely
- Handles file not found error
- Uses finally block

### Robust API Handling
- Handles ConnectionError
- Handles Timeout
- Handles generic exceptions

### Input Validation Loop
- Accepts product ID (1–100)
- Validates user input
- Fetches product details
- Handles 404 errors
- Exit using "quit"

---

## Task 4 — Error Logging

- Logs errors into error_log.txt
- Uses timestamp with datetime
- Handles:
  - Connection errors
  - HTTP errors (like 404)
- Displays log file content at the end

Example log entry:

[2026-04-03 01:05:10] ERROR in fetch_products: ConnectionError — No connection could be made

---

## How to Run

python part3_api_files.py

---

## Key Concepts Used

- File handling (read, write, append)
- Exception handling (try-except-finally)
- API calls using requests
- JSON parsing
- Input validation
- Logging with timestamps

---

## Notes

- DummyJSON API is a mock API (no real data is stored)
- Internet connection is required
- Error handling prevents crashes

---

## Author

Priyanka Raut

---

## Submission Checklist

- All tasks implemented
- Code runs without errors
- README.md added
- Repository is public
- error_log.txt contains logs