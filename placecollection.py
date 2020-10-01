"""name date etc..."""
from place import Place
from a1_classes import load_places
from operator import attrgetter


class PlaceCollection:
    """What this class does: """

    def __init__(self):
        self.places = []

    def __str__(self):
        return str([str(place) for place in self.places])

    def load_places(self, places_file):
        places = load_places()
        for place in places:
            name = place[0]
            country = place[1]
            priority = int(place[2])
            is_visited = place[3]
            new_place = Place(name, country, priority, is_visited)
            self.places.append(new_place)

    def save_places(self):
        pass

    def add_place(self, place):
        self.places.append(place)

    def get_unvisited(self):
        return len([place for place in self.places if not place.is_visited])

    def sort_places(self):
        pass
