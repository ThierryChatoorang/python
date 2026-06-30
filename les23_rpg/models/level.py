class Level:
    def __init__(self, name, description, enemies=None, items=None, exits=None):
        self.name = name
        self.description = description
        self.enemies = enemies if enemies is not None else []
        self.items = items if items is not None else []
        self.exits = exits if exits is not None else {}  # richting -> level_name

    def is_cleared(self):
        return all(not enemy.is_alive() for enemy in self.enemies)

    def levende_enemies(self):
        return [e for e in self.enemies if e.is_alive()]

    def remove_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                return item
        return None

    def __repr__(self):
        return f"Level({self.name})"
