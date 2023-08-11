import os
import hashlib
import requests
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import webbrowser
import mysql.connector
import datetime

# Set your VirusTotal API key
API_KEY = '29026cf065d9e500dc52916560d526fc5532441155b297d5d50acea00ae8d29c'

# Define a function to calculate the hash of a file
def get_file_hash(file_path):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    return hashlib.sha256(file_data).hexdigest()

# Define a function to scan a file using VirusTotal API
def scan_file(file_path):
    # ... (rest of the scan_file function)

# Define a function to show scan history
def show_scan_history():
    # ... (rest of the show_scan_history function)

# Define a function to handle the "Scan" button click event
def scan_button_click():
    # ... (rest of the scan_button_click function)

# Create a connection to your MySQL server
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='2006'
)
db_cursor = db_connection.cursor()

# Create the database if it doesn't exist
db_cursor.execute('CREATE DATABASE IF NOT EXISTS malware_scanner')
db_cursor.execute('USE malware_scanner')

# Create the table if it doesn't exist
db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS scan_results (
        id INT AUTO_INCREMENT PRIMARY KEY,
        file_path TEXT,
        positives INT,
        total INT,
        scan_datetime DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Commit the changes and close the cursor
db_connection.commit()
db_cursor.close()
db_connection.close()

# Create the main window
root = tk.Tk()
root.title('Malware Scanner')
root.geometry('500x400')

# Create the "Scan" button
scan_button = tk.Button(root, text='Scan', font=('Helvetica', 14), bg='#0095f6', fg='white', command=scan_button_click)
scan_button.pack(pady=20)

# Create the "Show History" button
show_history_button = tk.Button(root, text='Show History', font=('Helvetica', 14), bg='#ffa500', fg='white', command=show_scan_history)
show_history_button.pack(pady=10)

# Create the label to display the scan result
result_text = tk.Label(root, text='', font=('Helvetica', 14), bg='#fafafa', fg='#333')
result_text.pack(pady=10)

# Run the main event loop
root.mainloop()
