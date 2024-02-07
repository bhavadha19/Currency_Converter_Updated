import socket

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

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 12345

server.bind((host, port))
server.listen(5)

print(f"Server is listening on {host}:{port}")

while True:
    client, addr = server.accept()
    print(f"Connection from {addr}")

    data = client.recv(1024).decode()
    if not data:
        break

    try:
        base_currency, amount, target_currency = data.split(',')
        amount = float(amount)
        if base_currency in exchange_rates and target_currency in exchange_rates:
            converted_amount = amount * exchange_rates[target_currency] / exchange_rates[base_currency]
            client.send(str(converted_amount).encode())
        else:
            client.send("Invalid currencies".encode())
    except ValueError:
        client.send("Invalid input format".encode())

    client.close()

server.close()
