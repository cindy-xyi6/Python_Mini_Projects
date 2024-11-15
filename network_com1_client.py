import socket

# Define the server IP and port
server_ip = "192.168.0.43"  # Localhost
server_port = 60000      # Same port as the server

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define a message to send
message = "Hello, UDP server, hello!"

# Send the message to the server
client_socket.sendto(message.encode(), (server_ip, server_port))

# Receive a response from the server
response, server_address = client_socket.recvfrom(1024)
print(f"Received from server: {response.decode()}")

# Close the socket
client_socket.close()
 