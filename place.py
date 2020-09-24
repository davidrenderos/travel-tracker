"""name date etc..."""


# Create your Place class in this file


class Place:
    """What this class does: """

    def __init__(self, name="", country="", priority=0, is_visited=False):
        self.name = name
        self.country = country
        self.priority = priority
        self.is_visited = is_visited

    def __str__(self):
        return "{}, {}, {}, {}".format(self.name, self.country, self.priority, self.is_visited)

    def visited(self):
        pass
        # return self.is_visited == True

    def unvisited(self):
        pass

    def important_place(self):
        pass
