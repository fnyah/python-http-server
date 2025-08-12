import socket

# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the content of htdocs/index.html
    with open('htdocs/index.html') as fin:
        content = fin.read()

    # Send HTTP response with proper headers
    response = (
        'HTTP/1.0 200 OK\r\n'
        'Content-Type: text/html\r\n'
        f'Content-Length: {len(content.encode())}\r\n'
        '\r\n'
        f'{content}'
    )
    client_connection.sendall(response.encode())
    client_connection.close()  # Properly close the connection

# Close socket
server_socket.close()
