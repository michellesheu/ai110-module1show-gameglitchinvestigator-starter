from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_check_guess_hint_messages_are_not_swapped():
    """
    Regression test for swapped Higher/Lower hints bug.
    Verifies that hint messages correctly guide the player:
    - When guess is too high, message should say "Go LOWER!"
    - When guess is too low, message should say "Go HIGHER!"
    """
    secret = 50

    # Test guess too high
    outcome_high, message_high = check_guess(60, secret)
    assert outcome_high == "Too High"
    assert "LOWER" in message_high, f"Expected 'LOWER' in hint but got: {message_high}"
    assert "HIGHER" not in message_high, f"Hint should not say 'HIGHER' when guess is too high: {message_high}"

    # Test guess too low
    outcome_low, message_low = check_guess(40, secret)
    assert outcome_low == "Too Low"
    assert "HIGHER" in message_low, f"Expected 'HIGHER' in hint but got: {message_low}"
    assert "LOWER" not in message_low, f"Hint should not say 'LOWER' when guess is too low: {message_low}"


def test_get_range_for_difficulty_easy():
    """Test that Easy difficulty returns the correct range (1-20)."""
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20


def test_get_range_for_difficulty_normal():
    """Test that Normal difficulty returns the correct range (1-100)."""
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100


def test_get_range_for_difficulty_hard():
    """Test that Hard difficulty returns the correct range (1-200)."""
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 200


def test_difficulty_ranges_are_progressive():
    """
    Regression test for state bug: secret number regeneration should respect difficulty.
    Verifies that Hard is actually harder (larger range) than Normal, which is harder than Easy.
    """
    easy_low, easy_high = get_range_for_difficulty("Easy")
    normal_low, normal_high = get_range_for_difficulty("Normal")
    hard_low, hard_high = get_range_for_difficulty("Hard")

    # Easy range should be smaller than Normal
    easy_range = easy_high - easy_low
    normal_range = normal_high - normal_low
    hard_range = hard_high - hard_low

    assert easy_range < normal_range, "Easy should have fewer numbers than Normal"
    assert normal_range < hard_range, "Normal should have fewer numbers than Hard"
