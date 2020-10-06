"""(Incomplete) Tests for Place class."""
from place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print("{}\n".format(default_place))
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)
    print("{}\n".format(new_place))
    assert new_place.name == "Malagar"
    assert new_place.country == "Spain"
    assert new_place.priority == 1
    assert new_place.is_visited is False

    # Test mark as visited
    print("Mark as visited:")
    unvisited_place = Place("Sydney", "Australia", 3, False)
    print("Expect False got {}".format(unvisited_place.is_visited))
    unvisited_place.mark_visited()
    print("Expect True got {}\n".format(unvisited_place.is_visited))
    assert unvisited_place.is_visited is True

    # Test mark as unvisited
    print("Mark as unvisited:")
    visited_place = Place("Tokyo", "Japan", 1, True)
    print("Expect True got {}".format(visited_place.is_visited))
    visited_place.mark_unvisited()
    print("Expect False got {}\n".format(visited_place.is_visited))
    assert visited_place.is_visited is False

    # Test unimportant place
    print("Test unimportant place:")
    important_place = Place("New York", "USA", 4, False)
    print("Expect False got {}\n".format(Place.is_important_place(important_place)))

    # Test important place
    print("Test important place:")
    unimportant_place = Place("Madrid", "Spain", 1, False)
    print("Expect True got {}\n".format(Place.is_important_place(unimportant_place)))


run_tests()
