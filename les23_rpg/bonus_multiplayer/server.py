"""
Simpele single-client RPG-server.

Protocol:
- Client stuurt tekstcommando's zoals "LOOK", "FIGHT", "TAKE potion",
  "USE potion", "GO east", "STATUS", "QUIT".
- Server stuurt telkens een tekstantwoord terug.

Dit is een single-client server: 1 speler tegelijk kan verbinden en spelen.
Multiplayer met 2 spelers en beurten is een uitdagende uitbreiding (zie README).
"""

import socket

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from models.player import Player
from models.enemy import Enemy
from models.item import Item
from models.level import Level
from game import Game

HOST = "127.0.0.1"
PORT = 5050


def maak_levels():
    forest = Level(
        name="Forest",
        description="Je staat in een donker bos.",
        enemies=[Enemy("Wolf", hp=20, attack_power=5)],
        items=[Item("Potion", "heal", 20)],
        exits={"east": "Cave"},
    )
    cave = Level(
        name="Cave",
        description="Een vochtige grot.",
        enemies=[Enemy("Goblin", hp=30, attack_power=8)],
        items=[Item("Sword", "attack_boost", 5)],
        exits={"west": "Forest"},
    )
    return {"Forest": forest, "Cave": cave}


class NetworkGame(Game):
    """Game-variant die output verzamelt in een string i.p.v. direct te printen,
    zodat we het antwoord over het netwerk kunnen versturen."""

    def __init__(self, player, levels, start_level):
        super().__init__(player, levels, start_level)
        self.buffer = []

    def _print(self, tekst):
        self.buffer.append(str(tekst))

    def verwerk(self, commando):
        self.buffer = []
        # we hergebruiken handle_command, maar vangen prints af via redirect
        import io
        import contextlib

        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.handle_command(commando)
            self.check_end()

        return output.getvalue()


def main():
    player = Player("Speler", hp=100, attack_power=10)
    levels = maak_levels()
    game = NetworkGame(player, levels, start_level="Forest")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server luistert op {HOST}:{PORT}...")

    conn, addr = server_socket.accept()
    print(f"Client verbonden vanaf {addr}")

    with conn:
        conn.sendall("Welkom! Typ LOOK, FIGHT, TAKE <item>, USE <item>, GO <richting>, STATUS of QUIT.\n".encode("utf-8"))

        while game.running:
            data = conn.recv(1024)
            if not data:
                break

            commando = data.decode("utf-8").strip()
            print(f"Ontvangen: {commando}")

            antwoord = game.verwerk(commando)
            if not antwoord.strip():
                antwoord = "(geen output)"

            conn.sendall(antwoord.encode("utf-8"))

            if commando.lower() == "quit" or not game.running:
                break

    server_socket.close()
    print("Server gestopt.")


if __name__ == "__main__":
    main()
