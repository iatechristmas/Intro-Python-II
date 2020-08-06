from room import Room
from item import Item
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# List all items

item = {
    'kokiri_sword': Item("Kokiri Sword", "This is a hidden treasure of the Kokiri, but you can borrow it for a while. Be sure to practice with it before you really fight!"),
    'deku_shield': Item("Deku Shield", "You got a Deku Shield! Switch to the Equipment Subscreen and select the shield. Press (A) to equip it. Press (R) to crouch and defend. If you press (R) while (Z) Targeting, you can move while defending."),
    'heart-container': Item("Heart Container", "You got a Heart Container! Your maximum life energy is increased by one heart. Your life energy will be totally filled."),
    'bomb': Item("Bomb", "Bomb! Link can overpower the enemy with the explosive blast of a bomb."),
    'small_key': Item("Small Key", "You got a Small Key! Use it to open a locked door. You can use the key only in this dungeon."),
    'boss_key': Item("Boss Key", "You got the Boss Key! Now you can get inside the chamber where the Boss lurks."),
    'deku_stick': Item("You got a Deku Stick! On the Select Item Subscreen, you can set it to (<), (v) or (>). Set it to (C) and swing it with (C)! When you want to put it away, stand still and press (A). You can carry up to 10 sticks, but don't waste them."),
    'deku_nut': Item("Deku Nut", "You got a Deku Nut! On the Select Item Subscreen, you can set it to (<), (v) or (>). Set it to (C) and try throwing it! It will flash and stun the enemy!")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Add items to rooms

room['outside'].list.append(items['kokiri_sword'])
room['outside'].list.append(items['deku_shield'])
room['foyer'].list.apppend(items['bomb'])
room['foyer'].list.apppend(items['small_key'])
room['overlook'].list.apppend(items['deku_stick'])
room['overlook'].list.apppend(items['deku_nut'])
room['treasure'].list.apppend(items['boss_key'])
room['treasure'].list.apppend(items['heart_container'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player("Link", "outside")

# Write a loop that:
#
welcome_message = f'What would you like to do?\nPress m to move\nPress i for inventory\nPress q to quit'

command = input(welcome_message)

def move_validation(direction):
    val = getattr(room[newPlayer.current_room], direction)
    if val != None:
        for key, value in room.items():
            if value == val:
                new_player.current_room = key
                print(f"\nItems Available: \n")
                for x in room[newPlayer.current_room].list:
                    print(f"{Room.getItems(x)}")
                print(f"\n{newPlayer}\nIs in room: {val.name} -- Description: {val.description}")
    else: 
        print(f"Player can't go there!")

while command != 'q':

    while command == m:

        move_message = f'Choose a direction\nPress n for North\nPress e for East\nPress s for South\nPress w for West\nPress m for Main Menu\nPress q to Quit'
        move_choice = input(move_message)
        if move_choice == "w":
            checkMove("n_to")
        elif move_choice == "a":
            checkMove("w_to")
        elif move_choice == "s":
            checkMove("s_to")
        elif move_choice == "d":
            checkMove("e_to")
        elif move_choice == "m":
            command = input(welcome_message)
        elif move_choice == "q":
            exit()
        else:
            print(f"Invalid input, please try again")

    while command == i:

        inventory_message = f'Choose what to do with your items\nType "take" to take an item\nType "drop" to drop an item\nPress m for Main Menu'
        inventory_choice = input(inventory_message)
        if "take" in inventory_choice:
            take_item(inventory_choice.split("take ")[1])
        elif "drop" in inventory_choice:
            drop_item(inventory_choice.split("drop ")[1])
        elif inventory_choice == "q":
            command = input(welcome_message)

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

