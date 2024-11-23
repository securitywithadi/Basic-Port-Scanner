import socket
host = input("Enter IP address to scan: ")
for port in range(1, 1025):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        if s.connect_ex((host, port)) == 0: print(f"Port {port} is open")
