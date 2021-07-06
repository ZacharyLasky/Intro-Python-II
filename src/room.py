# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    # def current_items(self):
    #     if len(self.items) > 0:
    #         room_items = [str(item) for item in self.items]
    #     else:
    #         room_items = "no items in room"
    #     print(f"Current room items: {room_items}")

