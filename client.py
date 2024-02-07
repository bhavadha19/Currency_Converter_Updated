import tkinter as tk
from tkinter import ttk
import socket

# Define exchange rates
exchange_rates = {
    "USD": 1.0,  # US Dollar
    "EUR": 0.85,  # Euro
    "GBP": 0.75,  # British Pound
    "JPY": 110.0,  # Japanese Yen
    "AUD": 1.35,  # Australian Dollar
    "CAD": 1.25,  # Canadian Dollar
    "CHF": 0.92,  # Swiss Franc
    "CNY": 6.45,  # Chinese Yuan
    "INR": 75.0,  # Indian Rupee
    "MXN": 20.0,  # Mexican Peso
    "SGD": 1.34,  # Singapore Dollar
    "ZAR": 15.0,  # South African Rand
}

def convert_currency():
    base_currency = base_currency_var.get()
    print("Base Currency:",base_currency)
    amount = amount_entry.get()
    print("Amount to be converted:",amount)
    target_currency = target_currency_var.get()
    print("Target currency:",target_currency)

    data = f"{base_currency},{amount},{target_currency}"
    client.send(data.encode())

    converted_amount = client.recv(1024).decode()
    print("Converted Amount:",converted_amount)
    result_label.config(text=f"Converted amount: {converted_amount}",font=("Helvetica", 16))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 12345
client.connect((host, port))
print("Connection started")
window = tk.Tk()
window.title("Currency Converter")
window.geometry("400x300")

title_label = tk.Label(window, text="Currency Converter", font=("Helvetica", 16))
title_label.pack(side="top", pady=10)

base_currency_label = tk.Label(window, text="Base Currency:")
base_currency_label.pack(pady=10)

# Dropdown for base currency
base_currency_var = tk.StringVar()
base_currency_options = ttk.Combobox(window, textvariable=base_currency_var)
base_currency_options['values'] = list(exchange_rates.keys())
base_currency_options.pack()

amount_label = tk.Label(window, text="Amount:")
amount_label.pack()
amount_entry = tk.Entry(window)
amount_entry.pack()

target_currency_label = tk.Label(window, text="Target Currency:")
target_currency_label.pack()

# Dropdown for target currency
target_currency_var = tk.StringVar()
target_currency_options = ttk.Combobox(window, textvariable=target_currency_var)
target_currency_options['values'] = list(exchange_rates.keys())
target_currency_options.pack()

convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
