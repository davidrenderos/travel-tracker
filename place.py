"""
David Renderos
Assignment 2 - Travel Tracker
"""


class Place:
    """Holds characteristics of a Place"""
    IMPORTANCE = 2

    def __init__(self, name="", country="", priority=0, is_visited=False):
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def __str__(self):
        return "{self.name}, {self.country}, {self.priority}, {self.is_visited}".format(self=self)

    def mark_visited(self):
        self.is_visited = True

    def mark_unvisited(self):
        self.is_visited = False

    def is_important_place(self):
        return self.priority <= Place.IMPORTANCE
