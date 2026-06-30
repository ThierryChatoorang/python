from models.player import Player
from models.enemy import Enemy
from models.item import Item
from models.level import Level
from game import Game


def maak_levels():
    forest = Level(
        name="Forest",
        description="Je staat in een donker bos. Takken kraken om je heen.",
        enemies=[Enemy("Wolf", hp=20, attack_power=5)],
        items=[Item("Potion", "heal", 20)],
        exits={"east": "Cave"},
    )

    cave = Level(
        name="Cave",
        description="Een vochtige grot. Het druipt water van het plafond.",
        enemies=[Enemy("Goblin", hp=30, attack_power=8)],
        items=[Item("Sword", "attack_boost", 5)],
        exits={"west": "Forest", "north": "Boss Room"},
    )

    boss_room = Level(
        name="Boss Room",
        description="Een grote stenen kamer. Je voelt een dreigende aanwezigheid.",
        enemies=[Enemy("Dragon", hp=60, attack_power=15)],
        items=[],
        exits={"south": "Cave"},
    )

    return {
        "Forest": forest,
        "Cave": cave,
        "Boss Room": boss_room,
    }


def main():
    naam = input("Wat is de naam van je personage? ").strip() or "Held"
    player = Player(naam, hp=100, attack_power=10)

    levels = maak_levels()
    game = Game(player, levels, start_level="Forest")
    game.run()


if __name__ == "__main__":
    main()
