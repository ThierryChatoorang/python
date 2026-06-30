class Item:
    def __init__(self, name, item_type, value):
        """
        item_type: "heal" of "attack_boost"
        value: hoeveel hp/aanval het effect geeft
        """
        self.name = name
        self.type = item_type
        self.value = value

    def apply(self, player):
        if self.type == "heal":
            player.heal(self.value)
            return f"{player.name} gebruikt {self.name} en heelt {self.value} HP."

        elif self.type == "attack_boost":
            player.attack_power += self.value
            return f"{player.name} gebruikt {self.name} en krijgt +{self.value} attack."

        return f"{self.name} heeft geen bekend effect."

    def __repr__(self):
        return f"{self.name} ({self.type}, {self.value})"
