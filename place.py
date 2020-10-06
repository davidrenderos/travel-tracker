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
        return "{self.name}, {self.country}, {self.priority}, {self.is_visited}".format(self=self)

    def mark_visited(self):
        mark_asv = 'v' if self.is_visited else 'n'
        return mark_asv

    def mark_unvisited(self):
        mark_asn = 'v' if self.is_visited else 'n'
        return mark_asn

    def is_important_place(self):
        return self.priority >= Place.IMPORTANCE
