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

class MalwareScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Malware Scanner')
        self.root.geometry('500x400')

        # Create the "Scan" button
        self.scan_button = tk.Button(self.root, text='Scan', font=('Helvetica', 14), bg='#0095f6', fg='white', command=self.scan_button_click)
        self.scan_button.pack(pady=20)

        # Create the "Show History" button
        self.show_history_button = tk.Button(self.root, text='Show History', font=('Helvetica', 14), bg='#ffa500', fg='white', command=self.show_scan_history)
        self.show_history_button.pack(pady=10)

        # Create the label to display the scan result
        self.result_text = tk.Label(self.root, text='', font=('Helvetica', 14), bg='#fafafa', fg='#333')
        self.result_text.pack(pady=10)

    def scan_button_click(self):
        file_path = filedialog.askopenfilename(title='Select a file to scan')
        if file_path:
            hash_value = self.get_file_hash(file_path)
            self.scan_file(file_path, hash_value)

    def show_scan_history(self):
        db_connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='2006',
            database='malware_scanner'
        )
        db_cursor = db_connection.cursor()

        db_cursor.execute('SELECT * FROM scan_results')
        results = db_cursor.fetchall()

        history_text = "Scan History:\n"
        for result in results:
            history_text += f"File: {result[1]}, Positives: {result[2]}, Total: {result[3]}, Scan Time: {result[4]}\n"

        self.result_text.config(text=history_text)

        db_cursor.close()
        db_connection.close()

    def get_file_hash(self, file_path):
        with open(file_path, 'rb') as f:
            file_data = f.read()
        return hashlib.sha256(file_data).hexdigest()

    def scan_file(self, file_path, hash_value):
        # Implement VirusTotal API scanning here
        # ...
        positives = 0  # Replace with actual number of positives
        total = 0      # Replace with actual total number
        self.save_scan_result(file_path, positives, total)

    def save_scan_result(self, file_path, positives, total):
        db_connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='2006',
            database='malware_scanner'
        )
        db_cursor = db_connection.cursor()

        insert_query = "INSERT INTO scan_results (file_path, positives, total) VALUES (%s, %s, %s)"
        values = (file_path, positives, total)
        db_cursor.execute(insert_query, values)

        db_connection.commit()
        db_cursor.close()
        db_connection.close()

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
app = MalwareScannerApp(root)
root.mainloop()
