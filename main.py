"""
Name: David Renderos
Date: 26/10/2020
Brief Project Description: This project highlights the use of inheritance and the use of classes.
GitHub URL: https://github.com/cp1404-students/travel-tracker-assignment-2-davidrenderos
"""

from kivy.app import App
from placecollection import PlaceCollection
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.button import Button
from place import Place

VISITED = (1, 0, 0, 1)
UNVISITED = (1, 0, 1, 1)
PLACES_FILE = 'places.csv'
SORT_CATEGORIES = {'Name': 'name', 'Country': 'country', 'Priority': 'priority', 'Visited': 'is_visited'}


class TravelTrackerApp(App):
    """App constructor class, used for GUI"""
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
        return self.root

    def create_buttons(self):
        """Creates buttons from MovieCollection for the GUI."""
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

    def handle_press_add(self, new_name, new_country, new_priority):
        if self.validate_input(new_name, new_country, new_priority):
            self.place_collection.add_place(Place(new_name, new_country, int(new_priority), False))
            button = Button(text='{} in {}, priority {} added'.format(new_name, new_country, new_priority), id=new_name,
                            background_color=UNVISITED)
            button.bind(on_release=self.handle_press_place)
            button.place = self.place_collection.places[-1]
            self.clear_fields()
            self.update_place_buttons()

    def validate_input(self, name, country, priority):
        input_fields = name, country, priority
        for field in input_fields:
            if field == '':
                self.place_status = "All fields must be completed"
                return False
        try:
            priority = int(priority)
        except ValueError:
            self.place_status = "Please enter a valid number"
            return False
        if not priority > 0:
            self.place_status = "Priority must be >0"
            return False
        return True

    def clear_fields(self):
        self.root.ids.new_name.text = ''
        self.root.ids.new_country.text = ''
        self.root.ids.new_priority.text = ''
        self.place_status = ''

    def on_stop(self):
        self.place_collection.boolean_to_string()
        self.place_collection.save_places(PLACES_FILE)


if __name__ == '__main__':
    TravelTrackerApp().run()
