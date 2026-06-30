"""
Simpele RPG-client die verbindt met server.py en commando's stuurt.
"""

import socket

HOST = "127.0.0.1"
PORT = 5050


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    welkom = client_socket.recv(1024).decode("utf-8")
    print(welkom)

    while True:
        commando = input("> ").strip()
        if not commando:
            continue

        client_socket.sendall(commando.encode("utf-8"))

        if commando.lower() == "quit":
            break

        antwoord = client_socket.recv(4096).decode("utf-8")
        print(antwoord)

    client_socket.close()
    print("Verbinding gesloten.")


if __name__ == "__main__":
    main()
