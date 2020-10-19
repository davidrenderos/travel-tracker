"""..."""
# Copy your first assignment to this file, then update it to use Place class
# Optionally, you may also use PlaceCollection class

from place import Place
import csv
from operator import itemgetter

MENU = "Menu: \nL - List places \nA - Add new place \nM - Mark a place as visited \nQ - Quit"
PLACES_FILE = 'places.csv'
N = "n"
V = "v"


def main():
    """Contains all necessary functions needed for Assessment 1"""
    list_of_places = load_places()
    print("Travel Tracker 1.0 - by David Renderos")
    print("{} places loaded from {}".format(len(list_of_places), PLACES_FILE))
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            list_places(list_of_places)
        elif menu_choice == "A":
            add_place(list_of_places)
        elif menu_choice == "M":
            mark_visited(list_of_places)
        else:
            print("Invalid menu choice")
        print(MENU)
        menu_choice = input(">>> ").upper()
    print("{} places saved to {}\nHave a nice day :)".format(len(list_of_places), PLACES_FILE))
    save_places(list_of_places)


def load_places():
    """Start empty list for place storage; Load needed csv file"""
    list_of_places = []
    in_file = open(PLACES_FILE, 'r')
    reader = csv.reader(in_file)
    # Split place so priority is an integer, for use with itemgetter in list_places()
    places = [[index[0], index[1], int(index[2]), index[3]] for index in reader if index]
    for place in places:
        list_of_places.append(place)
    in_file.close()
    return list_of_places


def list_places(places):
    """List places based on visit status and priority"""
    count = 0
    places.sort(key=itemgetter(3, 2))
    # Makes a list of unvisited places.
    unvisited = [place for place in places if 'n' in place]
    max_length_name = max((len(name[0]) for name in places))
    max_length_country = max((len(country[1]) for country in places))
    for index in places:
        count += 1
        print_place = "{}. {:{}} in {:{}} priority {:>2}".format(count, index[0], max_length_name, index[1],
                                                                 max_length_country, index[2])
        if N in index[3]:
            print("*" + print_place)
        else:
            print(" " + print_place)
    if len(unvisited) > 0:
        print("{} places. You still want to visit {} places.".format(len(places), len(unvisited)))
    else:
        print("{} places. No places left to visit. Why not add a new place?".format(len(places)))


def add_place(places):
    """Add place to list_of_places"""
    priority = ""
    is_valid_priority = False
    name = input("Name: ")
    while name == "":
        print("Input cannot be blank")
        name = input("Name: ")
    country = input("Country: ")
    while country == "":
        print("Input cannot be blank")
        country = input("Country: ")
    while not is_valid_priority:
        try:
            priority = int(input("Priority: "))
            if priority < 1:
                print("Number must be > 0")
            else:
                is_valid_priority = True
        except ValueError:
            print("Invalid input; enter a valid number")
    print("{} in {} (priority {}) added to Travel Tracker".format(name, country, priority))
    places.append(Place)


def mark_visited(places):
    """Mark place as visited, take number for place to be marked, add new form of place to list_of_places"""
    places_unvisited = []
    for place in places:
        if N in place:
            places_unvisited.append(place)
    if not places_unvisited:
        print("No unvisited places")
    else:
        list_places(places)
        places_marked_visited = []
        for place in places:
            if V in place:
                places_marked_visited.append(place)
        valid_place_choice = False
        mark_as_visited = 0
        print("Enter the number of a place to mark as visited")
        while not valid_place_choice:
            try:
                mark_as_visited = int(input(">>> "))
                mark_as_visited -= 1
                if mark_as_visited < 0:
                    print("Number must be > 0")
                elif mark_as_visited > len(places):
                    print("Invalid place number")
                else:
                    valid_place_choice = True
            except ValueError:
                print("Invalid input; enter a valid number")
        if N in places[mark_as_visited]:
            print("{} in {} visited!".format(*places[mark_as_visited]))
            places_marked_visited.append(places[mark_as_visited])
        else:
            print("That place is already visited")
        for place in places_marked_visited:
            place[3] = "v"


def save_places(places):
    """Save file once MENU is (Q)uit, write to csv file with 'new' place list"""
    out_file = open(PLACES_FILE, 'w', newline='')
    writer = csv.writer(out_file)
    for place in places:
        writer.writerow(place)
    out_file.close()
    return places


if __name__ == '__main__':
    main()
