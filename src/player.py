# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def take_drop(self, takeDrop, itemName):
        if takeDrop == "take":
            for item in self.current_room.items:
                if itemName == str(item.name):
                    self.inventory.append(item)
                    self.current_room.items.remove(item)
                    print(f"You have picked up {item.name}")
                elif itemName != str(item.name):
                    print("That item is not here!")
        elif takeDrop == "drop":
            for item in self.inventory:
                if itemName == item.name:
                    self.inventory.remove(item)
                    self.current_room.items.append(item)
                    print(f"You have dropped {item.name}")
        else:
            print("Invalid command.")

    def move(self, string):
        if string == "n":
            if self.current_room.n_to == None:
                print("\nYou can't go in that direction!")
            else:
                self.current_room = self.current_room.n_to
        elif string == "s":
            if self.current_room.s_to == None:
                print("\nYou can't go in that direction!")
            else:
                self.current_room = self.current_room.s_to
        elif string == "e":
            if self.current_room.e_to == None:
                print("\nYou can't go in that direction!")
            else:
                self.current_room = self.current_room.e_to
        elif string == "w":
            if self.current_room.w_to == None:
                print("\nYou can't go in that direction!")
            else:
                self.current_room = self.current_room.w_to
        elif string == "q":
            print("\nThanks for playing!\n")
            quit()
        elif string == "i":
            print("Your inventory:")
            for each in self.inventory:
                print(f"{each.name}: {each.description}")
        else:
            print("Nonvalid command.")
