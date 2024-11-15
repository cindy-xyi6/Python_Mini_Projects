import socket

# Define the IP and port for the server
server_ip = "192.168.0.43"  # Localhost
server_port = 60000      # Arbitrary port for the server

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))

print(f"UDP server up and listening on {server_ip}:{server_port}")

# Loop to listen for incoming datagrams
while True:
    # Receive message from client
    message, client_address = server_socket.recvfrom(1024)  # Buffer size of 1024 bytes
    print(f"Received message from {client_address}: {message.decode()}")
    
    # Send a response back to the client
    response_message = "Message received, hello!"
    server_socket.sendto(response_message.encode(), client_address)
