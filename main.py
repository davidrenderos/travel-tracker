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

VISITED = (1, 0, 0, 1)
UNVISITED = (1, 0, 1, 1)
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
        self.places_to_visit = "Places to visit: {}".format(self.place_collection.get_unvisited())
        self.create_buttons()
        return self.root

    def create_buttons(self):
        for place in self.place_collection.places:
            display_color = self.set_button_color(place)
            button = Button(text=self.display_visited(place), id=place.name, background_color=display_color)
            button.bind(on_release=self.handle_press_place)
            button.place = place
            self.root.ids.place_box.add_widget(button)

    @staticmethod
    def set_button_color(place):
        display_color = UNVISITED
        if place.is_visited:
            display_color = VISITED
        return display_color

    def handle_press_place(self, instance):
        if instance.place.is_visited:
            instance.place.mark_unvisited()
        else:
            instance.place.mark_visited()
        instance.background_color = self.set_button_color(instance.place)
        place_instance = 'need to visit'
        if instance.place.is_visited:
            place_instance = 'visited'
        self.place_status = "You {} {}.".format(place_instance, instance.place.name)
        instance.text = self.display_visited(instance.place)
        self.places_to_visit = "Places to visit: {}".format(self.place_collection.get_unvisited())

    @staticmethod
    def display_visited(instance):
        is_visited = '(visited)'
        if not instance.is_visited:
            is_visited = ''
        button_display_text = instance.text = "{} in {}, priority {} {}".format(instance.name, instance.country,
                                                                                instance.priority, is_visited)
        return button_display_text

    def new_spinner_selection(self, new_sort_by):
        self.current_selection = new_sort_by
        self.update_place_buttons()

    def update_place_buttons(self):
        self.place_collection.sort_places(SORT_CATEGORIES[self.current_selection])
        self.root.ids.place_box.clear_widgets()
        self.create_buttons()


if __name__ == '__main__':
    TravelTrackerApp().run()
