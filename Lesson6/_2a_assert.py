from rock_paper_scissors_buggy import determine_winner, game_over, YOU, COMP


def assert_equals(actual, expected):
    assert actual == expected, f"Expected {expected}, got {actual}"


def test_determine_winner():
    assert_equals(determine_winner('r', 'r'), None)
    assert_equals(determine_winner('r', 'p'), COMP)
    assert_equals(determine_winner('r', 's'), YOU)
    assert_equals(determine_winner('p', 'r'), YOU)
    assert_equals(determine_winner('p', 'p'), None)
    assert_equals(determine_winner('p', 's'), COMP)
    assert_equals(determine_winner('s', 'r'), COMP)
    assert_equals(determine_winner('s', 'p'), YOU)
    assert_equals(determine_winner('s', 's'), None)

    print('determine_winner tests passed')


def test_game_over():
    assert_equals(game_over(3, [0, 0]), None)
    assert_equals(game_over(3, [1, 1]), None)
    assert_equals(game_over(3, [2, 1]), YOU)
    assert_equals(game_over(3, [1, 2]), COMP)
    assert_equals(game_over(5, [2, 2]), None)
    assert_equals(game_over(5, [3, 0]), YOU)
    assert_equals(game_over(5, [1, 3]), COMP)

    print('game_over tests passed')


test_determine_winner()
test_game_over()
