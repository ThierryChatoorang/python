class Game:
    def __init__(self, player, levels, start_level):
        """
        player: Player object
        levels: dict van level_name -> Level
        start_level: naam van het startlevel
        """
        self.player = player
        self.levels = levels
        self.current_level = self.levels[start_level]
        self.running = True

    def show_status(self):
        print(f"\n--- Status ---")
        print(f"Speler: {self.player.name} | HP: {self.player.hp}/{self.player.max_hp} | Attack: {self.player.attack_power}")
        print(f"Locatie: {self.current_level.name}")
        if self.player.inventory:
            items = ", ".join(item.name for item in self.player.inventory)
            print(f"Inventory: {items}")
        else:
            print("Inventory: (leeg)")

    def show_menu(self):
        print("\nActies: look | fight | take <item> | use <item> | go <richting> | status | quit")

    def look(self):
        print(f"\n{self.current_level.description}")

        enemies = self.current_level.levende_enemies()
        if enemies:
            print("Vijanden hier:")
            for i, enemy in enumerate(enemies):
                print(f"  {i}. {enemy}")
        else:
            print("Geen vijanden hier.")

        if self.current_level.items:
            namen = ", ".join(item.name for item in self.current_level.items)
            print(f"Items hier: {namen}")
        else:
            print("Geen items hier.")

        if self.current_level.exits:
            richtingen = ", ".join(self.current_level.exits.keys())
            print(f"Uitgangen: {richtingen}")

    def fight(self):
        enemies = self.current_level.levende_enemies()
        if not enemies:
            print("Er zijn hier geen vijanden om te bevechten.")
            return

        if len(enemies) == 1:
            enemy = enemies[0]
        else:
            for i, e in enumerate(enemies):
                print(f"{i}. {e}")
            keuze = input("Welke vijand aanvallen (nummer): ").strip()
            if not keuze.isdigit() or not (0 <= int(keuze) < len(enemies)):
                print("Ongeldige keuze.")
                return
            enemy = enemies[int(keuze)]

        print(self.player.attack(enemy))

        if not enemy.is_alive():
            print(f"{enemy.name} is verslagen!")
        else:
            self.enemy_turn(enemy)

    def enemy_turn(self, enemy=None):
        vijanden = [enemy] if enemy else self.current_level.levende_enemies()
        for e in vijanden:
            if e.is_alive() and self.player.is_alive():
                print(e.attack(self.player))

    def take(self, item_name):
        item = self.current_level.remove_item(item_name)
        if item is None:
            print(f"Geen item genaamd '{item_name}' gevonden.")
            return

        self.player.add_item(item)
        print(f"Je hebt {item.name} opgepakt.")

    def use(self, item_name):
        resultaat = self.player.use_item(item_name)
        print(resultaat)

    def go(self, richting):
        if richting not in self.current_level.exits:
            print(f"Je kunt niet naar '{richting}' vanaf hier.")
            return

        if not self.current_level.is_cleared():
            print("Er zijn hier nog levende vijanden! Versla ze eerst voordat je verder gaat.")
            return

        nieuw_level_naam = self.current_level.exits[richting]
        self.current_level = self.levels[nieuw_level_naam]
        print(f"Je loopt naar {self.current_level.name}.")
        self.look()

    def handle_command(self, cmd):
        cmd = cmd.strip()
        if not cmd:
            return

        delen = cmd.split(maxsplit=1)
        actie = delen[0].lower()
        argument = delen[1] if len(delen) > 1 else ""

        if actie == "look":
            self.look()
        elif actie == "fight":
            self.fight()
        elif actie == "take":
            if argument:
                self.take(argument)
            else:
                print("Gebruik: take <itemnaam>")
        elif actie == "use":
            if argument:
                self.use(argument)
            else:
                print("Gebruik: use <itemnaam>")
        elif actie == "go":
            if argument:
                self.go(argument)
            else:
                print("Gebruik: go <richting>")
        elif actie == "status":
            self.show_status()
        elif actie == "quit":
            self.running = False
        else:
            print("Onbekend commando. Typ 'look', 'fight', 'take', 'use', 'go', 'status' of 'quit'.")

    def check_end(self):
        if not self.player.is_alive():
            print(f"\n💀 {self.player.name} is gestorven. Game over.")
            self.running = False
            return True

        alle_levels_cleared = all(level.is_cleared() for level in self.levels.values())
        if alle_levels_cleared:
            print(f"\n🏆 Alle vijanden zijn verslagen! {self.player.name} wint het spel!")
            self.running = False
            return True

        return False

    def run(self):
        print(f"=== Welkom, {self.player.name}! ===")
        self.look()

        while self.running:
            self.show_menu()
            cmd = input("> ")
            self.handle_command(cmd)
            self.check_end()

        print("Bedankt voor het spelen!")
