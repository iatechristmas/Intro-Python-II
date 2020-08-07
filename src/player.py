# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init_(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.list = []

    def __str__(self):
        return f"Player: '{self.name}' {self.list}"

    def take_item(self, item):
        return f"You picked up {item}! It has been added to your inventory."

    def drop_item(self, item):
        return f"You dropped {item}! It has been added to your inventory."

