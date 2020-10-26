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
from kivy.uix.button import Button

PLACES_FILE = 'places.csv'
SORT_CATEGORIES = {'Name': 'name', 'Country': 'country', 'Priority': 'priority', 'Visited': 'is_visited'}


class TravelTrackerApp(App):
    """..."""
    current_selection = StringProperty()
    sort_by = ListProperty()
    places_to_visit = StringProperty()
    place_status = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.place_collection = PlaceCollection()
        self.place_collection.load_places(PLACES_FILE)

    def build(self):
        self.title = "Places To Visit 2.0"
        self.root = Builder.load_file('app.kv')
        self.sort_by = sorted(SORT_CATEGORIES.keys())
        self.current_selection = self.sort_by[0]
        self.places_to_visit = "Visit {}".format(self.place_collection.get_unvisited())
        self.create_buttons()
        return self.root

    def create_buttons(self):
        for place in self.place_collection.places:
            button = Button(text=place.name, id=place.name)
            button.bind(on_release=self.handle_press_place)
            button.place = place
            self.root.ids.box.add_widget(button)

    def handle_press_place(self, instance):
        place = instance.place
        visit_status_str = 'visited'
        if not place.is_visited:
            visit_status_str = 'unvisited'
        self.place_status = "{} {}".format(visit_status_str, place.name)

    def new_spinner_selection(self, new_sort_by):
        self.current_selection = new_sort_by
        print("Now:", new_sort_by)

if __name__ == '__main__':
    TravelTrackerApp().run()
