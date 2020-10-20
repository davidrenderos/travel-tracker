"""
Name:
Date:
Brief Project Description:
GitHub URL:
"""

from kivy.app import App
from placecollection import PlaceCollection
from kivy.lang import Builder

PLACES_FILE = 'places.csv'


class TravelTrackerApp(App):
    """..."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.place_collection = PlaceCollection()
        self.place_collection.load_places(PLACES_FILE)

    def build(self):
        self.title = "Places To Visit 2.0"
        self.root = Builder.load_file('app.kv')
        return self.root


if __name__ == '__main__':
    TravelTrackerApp().run()
