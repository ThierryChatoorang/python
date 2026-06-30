class Enemy:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def attack(self, player):
        player.take_damage(self.attack_power)
        return f"{self.name} valt {player.name} aan voor {self.attack_power} schade."

    def __repr__(self):
        return f"{self.name} (HP: {self.hp})"
