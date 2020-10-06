"""(Incomplete) Tests for PlaceCollection class."""
from placecollection import PlaceCollection
from place import Place


def run_tests():
    """Test PlaceCollection class."""

    # Test empty PlaceCollection (defaults)
    print("Test empty PlaceCollection:")
    place_collection = PlaceCollection()
    print(place_collection)
    assert not place_collection.places  # an empty list is considered False

    # Test get_unvisited method
    print("Test get_unvisited method:")
    p = PlaceCollection()
    place1 = Place("Sydney", "Australia", 3, True)
    place2 = Place("New York", "USA", 4, False)
    place3 = Place("Tokyo", "Japan", 1, True)
    p.add_place(place1)
    p.add_place(place2)
    p.add_place(place3)
    print(p)
    print("{} total unvisited places".format(p.get_unvisited()))

    # Test loading places
    print("Test loading places:")
    place_collection.load_places('places.csv')
    print(place_collection)
    assert place_collection.places  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Place with values
    # print("Test adding new place:")
    # place_collection.add_place(Place("Smithfield", "Australia", 5, False))
    # print(place_collection)

    # Test sorting places
    print("Test sorting - priority:")
    place_collection.sort("priority")
    print(place_collection)

    # Test sorting places
    print("Test sorting - name:")
    place_collection.sort("name")
    print(place_collection)

    # Test sorting places
    print("Test sorting - country:")
    place_collection.sort("country")
    print(place_collection)

    # Test sorting places
    print("Test sorting - visited:")
    place_collection.sort("is_visited")
    print(place_collection)
    # TODO: Test saving places (check CSV file manually to see results)

    # TODO: Add more tests, as appropriate, for each method


run_tests()
