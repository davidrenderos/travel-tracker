"""(Incomplete) Tests for Place class."""
from place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)
    print(new_place)
    assert new_place.name == "Malagar"
    assert new_place.country == "Spain"
    assert new_place.priority == 1
    assert new_place.is_visited is False

    # Test if visited
    print("Test if visited:")
    visited_place = Place("Sydney", "Australia", 3, True)
    print(visited_place)
    print(Place.get_visited(visited_place))
    assert visited_place.is_visited is True

    # Test if unvisited
    print("Test if unvisited:")
    unvisited_place = Place("Tokyo", "Japan", 1, False)
    print(unvisited_place)
    print(Place.get_unvisited(unvisited_place))
    assert unvisited_place.is_visited is False

    # Test important  place
    print("Test important place:")
    important_place = Place("New York", "USA", 4, False)
    print(important_place)
    print(Place.is_important_place(important_place))

    # Test unimportant  place
    print("Test unimportant place:")
    unimportant_place = Place("Madrid", "Spain", 1, False)
    print(unimportant_place)
    print(Place.is_important_place(unimportant_place))


run_tests()
