"""name date etc..."""
from place import Place
from operator import attrgetter


class PlaceCollection:
    """What this class does: """

    def __init__(self):
        self.places = []

    def __str__(self):
        return str([str(place) for place in self.places])

    def load_places(self, places_file):
        in_file = open(places_file, 'r')
        for line in in_file:
            parts = line.strip().split(',')
            place = Place(parts[0], parts[1], int(parts[2]), parts[3])
            self.places.append(place)
        in_file.close()

    def save_places(self):
        pass

    def add_place(self, place):
        self.places.append(place)

    def get_unvisited(self):
        return len([place for place in self.places if not place.is_visited])

    def sort(self, key):
        sort_status = ""
        if key == "name":
            sort_status = sorted(self.places, key=attrgetter('name'))
        if key == "country":
            sort_status = sorted(self.places, key=attrgetter('country'))
        if key == "priority":
            sort_status = sorted(self.places, key=attrgetter('priority'))
        elif key == "is_visited":
            sort_status = sorted(self.places, key=attrgetter('is_visited'))
        self.places = sort_status
