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

    def save_places(self, place_file):
        out_file = open(place_file, 'w')
        for place in self.places:
            out_file.write("{}\n".format(place))
        out_file.close()

    def add_place(self, place):
        self.places.append(place)

    def get_unvisited(self):
        return len([place for place in self.places if not place.is_visited])

    def sort_places(self, key):
        self.places.sort(key=attrgetter(key, 'name'))

    def boolean_to_string(self):
        for place in self.places:
            if place.is_visited:
                place.is_visited = 'V'
            else:
                place.is_visited = 'n'
