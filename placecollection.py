"""
David Renderos
Assignment 2 - Travel Tracker
"""
from place import Place
from operator import attrgetter

NAME_INDEX = 0
COUNTRY_INDEX = 1
PRIORITY_INDEX = 2
STATUS_INDEX = 3
VISITED = 'v'
UNVISITED = 'n'


class PlaceCollection:
    """Track the usage of Movie objects. """

    def __init__(self):
        self.places = []

    def __str__(self):
        return str([str(place) for place in self.places])

    def load_places(self, places_file):
        in_file = open('{}'.format(places_file), 'r')
        for line in in_file:
            parts = line.strip().split(',')
            place = Place(parts[NAME_INDEX], parts[COUNTRY_INDEX], int(parts[PRIORITY_INDEX]), True if parts
                                                                        [STATUS_INDEX] == VISITED else False)
            self.places.append(place)
        in_file.close()

    def save_places(self, place_file):
        out_file = open('{}'.format(place_file), 'w')
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
                place.is_visited = VISITED
            else:
                place.is_visited = UNVISITED
