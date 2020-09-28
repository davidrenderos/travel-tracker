"""name date etc..."""


# Create your PlaceCollection class in this file


class PlaceCollection:
    """What this class does: """

    def __init__(self):
        self.places = []

    def __str__(self):
        return str([str(place) for place in self.places])

    def load_places(self):
        pass

    def save_places(self):
        pass

    def add_place(self, place):
        self.places.append(place)

    def get_unvisited(self):
        return ["Unvisited" for place in self.places if not place.is_visited]

    def sort_places(self):
        pass
