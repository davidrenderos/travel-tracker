"""name date etc..."""


class Place:
    """What this class does: """
    IMPORTANCE = 2

    def __init__(self, name="", country="", priority=0, is_visited=False):
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def __str__(self):
        return "{}, {}, {}, {}".format(self.name, self.country, self.priority, self.is_visited)

    def get_visited(self):
        return self.is_visited is True

    def get_unvisited(self):
        return self.is_visited is False

    def is_important_place(self):
        return self.priority >= Place.IMPORTANCE
