# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

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
        else:
            print("Nonvalid command.")
