import sys
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mouth beckons."),

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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Declare all the items

item = {
    'stick': Item("stick", "A regular-looking stick."),
    'pebble': Item("pebble", "A smooth, round pebble."),
    'lantern': Item("lantern", "Somehow, the flame inside is still flickering."),
    'coin': Item("coin", "A shimmering, golden coin."),
    'beetle': Item("beetle", "Probably just wants to be left alone..."),
    'lock': Item("lock", "A rusted, broken lock."),
    'rug': Item("rug", "An old, dusty rug.")
}

# Put items into rooms

room['outside'].items.append(item['stick'])
room['outside'].items.append(item['pebble'])
room['foyer'].items.append(item['coin'])
room['foyer'].items.append(item['rug'])
room['overlook'].items.append(item['lantern'])
room['narrow'].items.append(item['beetle'])
room['treasure'].items.append(item['lock'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player("Allie", room['outside'])


while True:
    print(f"Items in room:")
    for each in player1.current_room.items:
            print(each.name)
    answer = input(
        f"\n{player1.name}'s location: {player1.current_room.name}. {player1.current_room.description} \n\nChoose n, s, e, w, i, q, take [item], drop [item]: ")
    if len(answer) == 1:
        player1.move(answer)
    else:
        takeOrDrop = answer.split()[0]
        itemName = answer.split()[1]
        player1.take_drop(takeOrDrop, itemName)

# print(player1.inventory)
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
