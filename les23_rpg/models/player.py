class Player:
    def __init__(self, name, hp=100, attack_power=10):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_power = attack_power
        self.inventory = []

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def attack(self, enemy):
        enemy.take_damage(self.attack_power)
        return f"{self.name} valt {enemy.name} aan voor {self.attack_power} schade."

    def add_item(self, item):
        self.inventory.append(item)

    def use_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                resultaat = item.apply(self)
                self.inventory.remove(item)
                return resultaat
        return f"{item_name} zit niet in je inventory."

    def __repr__(self):
        return f"{self.name} (HP: {self.hp}/{self.max_hp})"
