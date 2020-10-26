"""
Name:
Date:
Brief Project Description:
GitHub URL:
"""

from kivy.app import App
from placecollection import PlaceCollection
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty

PLACES_FILE = 'places.csv'
SORT_CATEGORIES = ['name', 'country', 'priority', 'is visited']


class TravelTrackerApp(App):
    """..."""
    current_selection = StringProperty()
    sort_by = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.place_collection = PlaceCollection()
        self.place_collection.load_places(PLACES_FILE)

    def build(self):
        self.title = "Places To Visit 2.0"
        self.root = Builder.load_file('app.kv')
        self.sort_by = sorted(SORT_CATEGORIES)
        self.current_selection = self.sort_by[0]
        return self.root


if __name__ == '__main__':
    TravelTrackerApp().run()
