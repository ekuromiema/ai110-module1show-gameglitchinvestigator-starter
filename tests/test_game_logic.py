from logic_utils import check_guess

# --- Regression tests for the flipped-direction bug ---
# Original bug: check_guess paired "Too High" with "Go HIGHER!" and
# "Too Low" with "Go LOWER!", so the hint shown to the player pointed
# the wrong way (e.g. guess 97, secret 14 told the player to go HIGHER).

def test_too_high_hint_tells_player_to_go_lower():
    # The exact reported scenario: guess above the secret must say LOWER.
    outcome, message = check_guess(97, 14)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()
    assert "HIGHER" not in message.upper()


def test_too_low_hint_tells_player_to_go_higher():
    outcome, message = check_guess(5, 14)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()
    assert "LOWER" not in message.upper()


def test_large_guess_not_misjudged_by_string_comparison():
    # Original bug: the secret was stringified on even attempts, making the
    # comparison lexicographic ("100" < "14"), so 100 was wrongly called
    # "Too Low". Numeric comparison must report "Too High" -> go LOWER.
    outcome, message = check_guess(100, 14)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()
